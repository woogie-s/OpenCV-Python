# 5-01. 영상의 이동 변환과 전단 변환 - 전단 변환

import sys
import numpy as np
import cv2

src = cv2.imread('ref/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# x축 방향으로 층 밀림 변환, float 타입으로 지정해야함.
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

# 밀린 영상을 모두 보기 위해 출력 영상 크기를 구함.
# 출력 영상 크기를 지정할때는 int형
h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()