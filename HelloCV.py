import sys
import cv2 as cv

print("Hello OpenCV", cv.__version__)

img = cv.imread("assets/miru.jpeg")

if img is None:
    print("Image load failed!")
    sys.exit()

cv.namedWindow("image")
cv.imshow("image",img)
cv.waitKey()

cv.destroyAllWindows()