# 2-02. 영상의 생성, 복사, 부분 영상 추출

import numpy as np
import cv2

img1 = np.empty((240, 320), dtype=np.uint8)     # 픽셀값이 랜덤
img2 = np.zeros((240, 320, 3), dtype=np.uint8)
img3 = np.ones((240, 320, 3), dtype=np.uint8) * 255
img4 = np.full((240, 320), 128, dtype=np.uint8)

# 새 영상 생성하기
# img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image
# img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image
# img3 = np.ones((240, 320), dtype=np.uint8) * 255  # dark gray
# img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8)  # yellow

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('ref/HappyFish.jpg')

img2 = img1
img3 = img1.copy()

img1[:,:] = (0, 255, 255)   #img2도 같이 변함

#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('ref/HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0)    #img2를 0으로 채우면 img1도 그부분에 대해 0으로 채워짐

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
