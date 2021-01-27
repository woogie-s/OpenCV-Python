# 4-05. 잡음 제거 (1) - 미디언 필터
# salt & pepper 잡읍 제거에 효과적
# 영상 화질 quality 측면에서는 효과적이지 않음

import sys
import numpy as np
import cv2

src = cv2.imread('ref/noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 입력영상 src, 커널크기 3(1보다 큰 홀수)
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()