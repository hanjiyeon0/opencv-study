import cv2

src = cv2.imread('assets/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('assets/mask_plane.bmp', cv2.IMREAD_GRAYSCALE) 
dst = cv2.imread('assets/field.bmp', cv2.IMREAD_COLOR)
cv2.copyTo(src, mask, dst)

# Numpy의 Boolean Indexing을 이용한 마스크 연산
dst[mask>0] = src[mask>0]

cv2.imshow("src", src)
cv2.waitKey()
cv2.imshow("mask", mask)
cv2.waitKey()
cv2.imshow("dst", dst)
cv2.waitKey()