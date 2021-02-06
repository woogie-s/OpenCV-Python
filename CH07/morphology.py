# 7-04. 모폴로지(1) 침식과 팽창

import sys
import numpy as np
import cv2

src = cv2.imread('ref/circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# kernel 생성 함수
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))

# 모폴로지 침식, 팽창 연산
# kernel은 None 지정 시 3x3 사각형 구성 요소 사용
dst1 = cv2.erode(src, se)
dst2 = cv2.dilate(src, None)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# 구조 요소 모양 나타내는 플래그
# cv2.MORPH_RECT(사각형 모양)
# cv2.MORPH_CROSS(십자가 모양)
# cv2.MORPH_ELLIPSE(사각형에 내접하는 타원 모양)