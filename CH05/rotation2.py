# 5-04. 영상의 회전 (2)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 영상의 가운데 점 cp
cp = (src.shape[1] / 2, src.shape[0] / 2)
# cp점을 기준으로 반시계방향 20도, scaling 0.5
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 회전 변환 원리
# 1. 가운데 점을 원점에 위치시킨다.
# 2. 회전 변환
# 3. 이동한 만큼 다시 반대로 이동