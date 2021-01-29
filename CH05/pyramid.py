# 5-03. 이미지 피라미드
# 하나의 영상에 대해 다양한 해상도의 영상 세트를 구성하는 것
# 보통 가우시안 블러링 & 다운 샘플링 형태로 축소하여 구성

import sys
import numpy as np
import cv2

src = cv2.imread('ref/cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rc = (250, 120, 200, 200)  # rectangle tuple (x, y, w, h)

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)     # shift는 좌표를 얼마나 줄일지
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()

# cv2.pryDown(src, dst=None, dstsize=None, borderType=None)
# 입력영상 src, 출력영상 dst
# 출력영상 크기 dstsize(지정하지 않으면 가로,세로 크기의 1/2)
# 가장자리 픽셀 확장 방식 borderType
# 먼저 5x5크기의 가우시안 필터 적용 후 짝수 행과 열을 제거하는 방식

# cv2.pryUp(src, dst=None, dstsize=None, borderType=None)
