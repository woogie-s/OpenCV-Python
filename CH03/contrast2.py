# 3-05. 영상의 명암비 조절 (2)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
# 입력영상 src, 결과 dst None(무시), 알파(최소값) 0, 베타(최대값) 255, NORM_TYPE은 MINMAX(최소 최대값)

gmin = np.min(src)
gmax = np.max(src)
# 실수형태 계산을 위해 255.
# dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
