# 7-03. 지역 이진화 (1)
# 균일하지 않은 조명의 영향을 해결
# 픽셀 주변에 작은 윈도우를 설정하여 지역 이진화

import sys
import numpy as np
import cv2

# 입력 영상 불러오기
src = cv2.imread('ref/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 전역 이진화 by Otsu's method
_, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화 by Otsu's method
dst2 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] // 4

# 4X4 윈도우 크기로 지역 이진화
for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]       # dst2와 dst_는 픽셀 값 공유
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)  # 출력 값 dst_를 입력 값으로 주어 dst2에 공유되도록 

# 결과 출력
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
