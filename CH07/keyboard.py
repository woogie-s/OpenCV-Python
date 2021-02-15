# 7-06. 레이블링
# 동일 객체에 속한 모든 픽셀에 고유한 번호를 매기는 작업

import sys
import numpy as np
import cv2

src = cv2.imread('ref/keyboard.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 이진화된 src 영상 src_bin
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# 객체 개수+1 cnt, 레이블 맵행렬 labels, 각 객체의 바운딩 박스 stats, 각 객체의 무게중심위치정보 centroids
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    # 중간중간 노이즈를 검출하지 않게하기 위해
    if area < 20:
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()