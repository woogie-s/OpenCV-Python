# 3-07. 특정 색상 영역 추출하기 (2)

import sys
import numpy as np
import cv2

src = cv2.imread('ref/candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# pos를 따로 쓰지 않고 getTrackbarPos함수 이용
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')       # 'H_min'트랙바의 위치
    hmax = cv2.getTrackbarPos('H_max', 'dst')       # 'H_max'트랙바의 위치

    # H - hmin ~ hmax, S - 150~255, V - 0~255
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)


cv2.imshow('src', src)
cv2.namedWindow('dst')

# 트랙바 생성
cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()
