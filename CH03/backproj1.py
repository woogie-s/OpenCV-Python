# 3-08. 히스토그램 역투영 (1)
# 영상의 각 픽셀이 주어진 히스토그램 모델에 얼마나 일치하는지를 검사하는 방법
# 임의의 색상 영역을 검출할 때 효과적

import sys
import numpy as np
import cv2

# 입력 영상에서 ROI를 지정하고, 히스토그램 계산

src = cv2.imread('ref/cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

# 마우스를 이용해 어떤 영역을 선택할 수 있음
x, y, w, h = cv2.selectROI(src)

# --히스토그램 계산--
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]

channels = [1, 2]       # Cr, Cb 채널만 이용, Y(밝기) 채널은 사용 X
cr_bins = 128           # 256 이지만 128로 단순화
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv2.calcHist([crop], channels, None, histSize, ranges)
# ---

hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대해 히스토그램 역투영

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()


# Hue값을 이용해 색상을 숫자로 표현하기 좋을 때(빨주노초파남보) -> HSV
# 임의의 컬러를 표현하기에 적합한 것은 YCrCb, LAB