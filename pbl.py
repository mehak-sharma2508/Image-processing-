import cv2
import numpy as np
# Read input image
image = cv2.imread("fruit.jpg")
# Convert BGR image to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Define color threshold
lower = np.array([0, 50, 50])
upper = np.array([30, 255, 255])
# Create binary mask
mask = cv2.inRange(hsv, lower, upper)
# Apply morphological operations
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# Extract fruit region
segmented = cv2.bitwise_and(image, image, mask=mask)
# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Binary Mask", mask)
cv2.imshow("Segmented Fruit", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()::