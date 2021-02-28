# 8-01. 그랩컷 (1)

import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('ref/nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할(초기 객체의 위치를 지정)
rc = cv2.selectROI(src)         #(x, y, w, h)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0(cv2.GC_BGD), 2(cv2.GC_PR_BGD)를 0으로 설정, 나머지(1,3)를 1로 설정
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[..., np.newaxis]

mask = mask * 64

# 초기 분할 결과 출력
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
