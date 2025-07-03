import cv2
import mediapipe as mp

# Setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

# Tip landmark IDs for each finger
tip_ids = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_text = "No hand detected"

    if result.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(result.multi_hand_landmarks, result.multi_handedness):
            # Get handedness (Left/Right)
            label = hand_info.classification[0].label  # "Left" or "Right"

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmarks
            landmarks = hand_landmarks.landmark
            fingers = []

            # Thumb (logic depends on hand label)
            if label == "Right":
                if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:  # Left hand
                if landmarks[tip_ids[0]].x > landmarks[tip_ids[0] - 1].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 fingers (common logic)
            for id in range(1, 5):
                if landmarks[tip_ids[id]].y < landmarks[tip_ids[id] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = sum(fingers)
            finger_text = f"{label} hand: {total} finger(s)"

            # Show finger count per hand
            cv2.putText(frame, finger_text, (20, 60 if label == "Right" else 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    else:
        cv2.putText(frame, finger_text, (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
