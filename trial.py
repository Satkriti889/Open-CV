import cv2

# Load the image
image = cv2.imread("image.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Get image height and width
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

# Extracting RGB values at (100, 100)
(B, G, R) = image[100, 100]
print("R = {}, G = {}, B = {}".format(R, G, B))

# Extracting only the Blue channel
B = image[100, 100, 0]
print("B = {}".format(B))

# Extracting a Region of Interest (ROI)
roi = image[100:500, 200:700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Resize the image to fixed size
resize_fixed = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image (500x500)", resize_fixed)
cv2.waitKey(0)

# Resize the image while keeping the aspect ratio
ratio = 800 / w
dim = (800, int(h * ratio))
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized with Aspect Ratio", resize_aspect)
cv2.waitKey(0)

# Draw rectangle on the image (coordinates must be in (x1, y1) -> (x2, y2))
# Ensure (x1, y1) is top-left and (x2, y2) is bottom-right
output = image.copy()
rectangle = cv2.rectangle(output, (600, 400), (1500, 900), (255, 0, 0), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Add text on the image
output_text = image.copy()
text = cv2.putText(output_text, 'OpenCV Demo', (500, 550),
                   cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
cv2.imshow("Text", output_text)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
