import cv2

img1 = cv2.imread('assets/dog.jpeg')
#img2 = img1
#img3 = img1.copy()
 
#img1.fill(255)
img2 = img1[40:120, 30:150] # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()
img2.fill(0)

cv2.imshow("img", img1)
cv2.waitKey()
cv2.imshow("img", img2)
cv2.waitKey()
cv2.imshow("img", img3)
cv2.waitKey()