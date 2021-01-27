# 03. 블러링 (2) - 가우시안 필터 (1)
# mean = median = mode

import sys
import numpy as np
import cv2

src = cv2.imread('ref/rose.bmp', cv2.IMREAD_GRAYSCALE)

# 입력영상 src, ksize (0, 0)주면 sigma 값에 의해 자동 결정됨, sigma 값 3
dst = cv2.GaussianBlur(src, (0, 0), 3)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()