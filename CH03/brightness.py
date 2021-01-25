# 3-01. 영상의 밝기 조절

import sys
import numpy as np
import cv2

# 그레이스케일 영상 불러오기
src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, 100)
# dst = src + 100         # 255보다 커질 경우에 src - 255에 해당하는 값이 저장됨
# src + 100뒤에 .을 하나 찍어서 실수 단위로 계산되게 해야함.
# 그 후 astype함수를 이용해 uint8로 conversion 해줘야함.
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('ref/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()
# dst = cv2.add(src, 100)     # 100만 입력할 경우 (100,0,0,0) 튜플이 입력됨
dst = cv2.add(src, (100, 100, 100, 0))
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
