# 6-01. 영상의 미분과 소베 필터

import sys
import numpy as np
import cv2


src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0, delta=128)    # x 방향 1차 미분
dy = cv2.Sobel(src, -1, 0, 1, delta=128)    # y 방향 1차 미분

'''
kernel = np.array([[-1, 0, 1], 
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)

# delta 만큼 결과에 더함
# delta를 주지 않으면 값이 급격하게 감소한부분(밝->검)은 검게 나옴
dx = cv2.filter2D(src, -1, kernel, delta=128)
'''

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
