# 6-05. 허프 원 변환 원 검출

import sys
import numpy as np
import cv2

# 입력 이미지 불러오기
src = cv2.imread('ref/dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1.0)       # 노이즈 제거 및 디테일 감소 (성능 향상)

def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (cx, cy), int(radius), (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# 트랙바 생성
cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()

# 입력 영상과 동일한 2차원 평면 공간에서 축적영상 생성
# 에지 픽셀에서 그래디언트 계산
# 에지 방향에 따라 직선을 그리면서 값을 누적
# 원의 중심 먼저 찾고 적절한 반지름 검출(반지름을 늘려가면서)

# cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None,
#                 param2=None, minradius=None, maxRadius=None))
# 출력 : (cx, cy, r) np.ndarray.shape = (1, N, 3), dtype = np,float32
# 입력영상 image, 입력영상과 축적 배열의 크기 비율(dp), 검출된 원의 최소거리 (minDist)
# Cannsy 에지 검출기의 높은 임계값 (param1), 축적 배열에서 원 검출을 위한 임계값(param2)
# 검출할 원의 최소 최대 반지름 (minRadius, maxRadius)
