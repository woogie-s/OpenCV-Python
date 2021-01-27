# 4-02. 블러링(1) - 평균값 필터 (1)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# kernel = np.ones((3, 3), dtype=np.float64) / 9.
# 입력영상 src, -1(입력영상크기와 같게), 마스크 커널
# dst = cv2.filter2D(src, -1, kernel)
dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
