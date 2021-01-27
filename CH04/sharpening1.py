# 4-04. 샤프닝 - 언샤프 마스크 필터 (1)
# 그레이스케일 영상
import sys
import numpy as np
import cv2

src = cv2.imread('ref/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 우선 blur 영상을 만듬
blr = cv2.GaussianBlur(src, (0, 0), 2)
# sharpening 영상 = (src - blr) + src
# float형태로 연산 -> 2.0 *
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)
# dst = np.addweighted(src, 2, blr, -1, 0)      # 같은 방법

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
