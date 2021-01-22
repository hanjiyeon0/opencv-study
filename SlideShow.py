import os
import glob
import cv2

# 특정 폴더에 있는 이미지파일 목록 읽기
file_list = os.listdir("./assets")
img_files = [file for file in file_list if file.endswith(".jpeg")]
# img_files = glob.glob(".\\assets\\*.jpeg")

#전체화면 영상 출력 창 만들기
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#불러온 영상을 반복적으로 출력하기
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])
    if img is None:
        print('Image load failed!') 
        break
    cv2.imshow('image', img) 
    
    if cv2.waitKey(1000) >= 0:
        break
    
    idx += 1
    if idx >= cnt:
        idx = 0
 