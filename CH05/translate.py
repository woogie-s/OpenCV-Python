# 5-01. 영상의 이동 변환과 전단 변환 - 이동 변환

import sys
import numpy as np
import cv2

src = cv2.imread('ref/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 가로로 200, 세로로 100 이동, float 타입으로 지정해야함.
aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

# dsize를 (0, 0)을 주면 출력영상이 입력영상과 크기가 같게 출력됌
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()