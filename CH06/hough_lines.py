# 6-04. 허프 변환 직선 검출
# 2차원 영상 좌표에서 직선의 방정식을 파라미터 공간으로 변환하여 직선을 찾는 알고리즘

import sys
import numpy as np
import cv2

src = cv2.imread('ref/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)

# 입력에지영상 edges, 축적 배열에서 rho값의 간격, 축적 배열에서 theta 값의 간격
# threshold 160, 검출할 선분의 최소길이(minLineLength), 직선으로 간주할 최대 에지 점간격(maxLineGap)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.HoughLines 는 직선 파라미터(rho, theta)정보를 담고있는 np.ndarray를 반환(.shpae = (N, 1, 2), .dtype = numpy.float32)
# cv2.HoughLinesP 는 선분의 시작과 끝 좌표 정보(x1, y1, x2, y2)를 담고있는 np.ndarray를 반환(.shpae = (N, 1, 4), .dtype = numpy.int32)
