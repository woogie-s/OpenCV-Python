# 3-08. 히스토그램 역투영 (2)

import sys
import numpy as np
import cv2

# CrCb 살색 히스토그램 구하기
ref = cv2.imread('ref/kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('ref/kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)
# hist가 큰 값은 너무 큰 값이 나와서 큰 값 몇개만 밝게 나오는 경우가 있음
# 이를 해결하기 위해 log를 취해줌


# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('ref/kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
