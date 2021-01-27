# 4-06. 잡음 제거 (2) - 양방향 필터
# edge-preserving noise removal filter 중 하나
# 평균값 또는 가우시안 필터는 에지 부근에서 픽셀 값을 평탄하게 만드는 단점이 존재
# 기준 픽셀과 이웃 픽셀과의 거리, 그리고 픽셀 값의 차이를 함께 고려하여 블러링의 정도를 조절 

import sys
import numpy as np
import cv2

src = cv2.imread('ref/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)
# 입력영상 src,
# d(필터링에 사용될 이웃픽셀의 거리) -1(음수 입력 시 sigmaSpace 값에 의해 자동 결정)
# sigmaColor(색 공간에서 필터의 표준편차) 10 -> 에지 판단 기준
# sigmaSpace(좌표 공간에서 필터의 표준편차) 5 -> 가우시안 블러에서 sigma값과 비슷

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
