import cv2
import numpy as np

img = cv2.imread("/Users/vikas/PBL/flower.jpg")

if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

im1 = cv2.blur(img, (5, 5))

im2 = cv2.boxFilter(img, -1, (2, 2), normalize=True)

cv2.imshow("MEHAK Blurred (5x5) vs Box Filter (2x2)",
           np.hstack((im1, im2)))

cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
# img = cv2.imread("/Users/vikas/PBL/flower.jpg")
# dst = cv2.GaussianBlur(img, (5, 5), 0)
# cv2.imshow("MEHAK Original vs Gaussian Filter",
#            np.hstack((img, dst)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# img = cv2.imread("/Users/vikas/PBL/flower.jpg")
# if img is None:
#     print("Error: Image not found.")
#     exit()
# dst = cv2.medianBlur(img, 5)
# cv2.imshow("Original Image - MEHAK", img)
# cv2.imshow("Median Filter - MEHAK", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# img = cv2.imread("/Users/vikas/PBL/flower.jpg")
# if img is None:
#     print("Error: Image not found or path is incorrect.")
#     exit()
# dst = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow("MEHAK Original vs Bilateral Filter",
#            np.hstack((img, dst)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()