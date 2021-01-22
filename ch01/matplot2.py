import matplotlib.pyplot as plt
import cv2

# 컬러 영상 & 그레이스케일 영상 불러오기
imgBGR = cv2.imread("assets/miru.jpeg")
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread("assets/dog.jpeg", cv2.IMREAD_GRAYSCALE)

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis("off"), plt.imshow(imgRGB)
plt.subplot(122), plt.axis("off"), plt.imshow(imgGray, cmap="gray")
plt.show()