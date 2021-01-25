# 3-07. 특정 색상 영역 추출하기 (1)

import sys
import numpy as np
import cv2


# src = cv2.imread('ref/candies.png')
src = cv2.imread('ref/candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# B 0~100, G 128~255, R 0~100
dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
# H 50~80, S 150~255, V 0~255
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
