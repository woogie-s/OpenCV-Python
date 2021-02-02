# 6-02. 그래디언트와 에지 검출
# 그래디언트 : x축 y축을 각각 편미분하여 벡터 형태로 표현한 것

import sys
import numpy as np
import cv2

src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# flaot 형으로 지정 (그래디언트 크기 계산하기위해)
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

# 2D벡터의 x좌표 행렬, y좌표 행렬
mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)     # cliping과 타입변환

# mag영상에서 120이 넘는 값들만 흰색으로 에지 검출
edge = np.zeros(src.shape[:2], np.uint8)
edge[mag > 120] = 255
#_, edge = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge)
cv2.waitKey()

cv2.destroyAllWindows()