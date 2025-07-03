import cv2
from pyzbar.pyzbar import decode

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Decode QR codes in the frame
    for code in decode(frame):
        data = code.data.decode('utf-8')
        x, y, w, h = code.rect

        # Draw rectangle around QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display decoded text
        cv2.putText(frame, data, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Show frame
    cv2.imshow("QR Code Scanner", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
