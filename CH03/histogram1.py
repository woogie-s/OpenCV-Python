# 3-04. 히스토그램 분석 (1)

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 그레이스케일 영상의 히스토그램
src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# src를 리스트 형태로 입력, 그레이스케일 [0], 마스크 None, bin의 개수 256, 범위 [0, 256]
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
# hist 일차원 행렬

cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()

# 컬러 영상의 히스토그램
src = cv2.imread('ref/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()
