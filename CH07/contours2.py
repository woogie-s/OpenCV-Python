# 7-07. 외곽선 검출 (2)

import sys
import random
import numpy as np
import cv2

src = cv2.imread('ref/milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 영상 이진화
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# cv2.RETR_LIST로 받았기 때문에 계층구조 필요 없음
contours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

h, w = src.shape[:2]
dst = np.zeros((h, w, 3), np.uint8)

# 모든 외곽선을 랜덤한 색상으로 표현
for i in range(len(contours)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()