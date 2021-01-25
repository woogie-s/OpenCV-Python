# 3-06. 히스토그램 평활화

import sys
import numpy as np
import cv2

# 그레이스케일 영상의 히스토그램 평활화
src = cv2.imread('ref/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 컬러 영상의 히스토그램 평활화
src = cv2.imread('ref/field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# RGB 색상 성분을 그대로 히스토그램 평활화를 수행하게 되면
# 색이 원래 색상과 다르게 변할 수 있음.
# 색상 정보는 그대로 유지하고 밝기 정보만을 이용하기 위해 YCrCb 정보를 이용
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb)

# 밝기 성분에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
