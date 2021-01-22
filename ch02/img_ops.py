import numpy as np
import cv2 as cv

img1 = np.empty((480, 640), dtype=np.uint8) # grayscale image 
img2 = np.zeros((480, 640, 3), dtype=np.uint8) # color image
img3 = np.ones((480, 640), dtype=np.uint8) * 255 # white
img4 = np.full((480, 640, 3), (0, 255, 255), dtype=np.uint8) # yellow

cv.imshow("image",img1)
cv.waitKey()
cv.imshow("image",img2)
cv.waitKey()
cv.imshow("image",img3)
cv.waitKey()
cv.imshow("image",img4)
cv.waitKey()

cv.destroyAllWindows()