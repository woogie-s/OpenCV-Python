# 3-05. 영상의 명암비 조절 (1)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0     # 기울기(대비 증가)
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
# 연산 결과를 clip함수를 이용해 0이하 255이상 값을 처리
# astype를 이용해 uint8 변환

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
