# 7-03. 지역 이진화 (2)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

def on_trackbar(pos):
    bsize = pos
    # 블록 크기 bsize는 3이상의 홀수이어야함
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    # 블록 평균 계산 방법(cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    # 블록 내 평균값 또는 블록 내 가중 평균값에서 뺄 값 C(5)
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, bsize, 5)

    cv2.imshow('dst', dst)


cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)

cv2.waitKey()
cv2.destroyAllWindows()

# 한 픽셀 단위로 블록 크기만큼 연산을 수행함 (연산이 조금 느릴 수 있음)