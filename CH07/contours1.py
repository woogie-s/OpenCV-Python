# 7-07. 외곽선 검출 (1)
# 객체의 외곽선 좌표를 모두 추출하는 작업

import sys
import random
import numpy as np
import cv2

src = cv2.imread('ref/contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 외곽선 검출모드 cv2.RETR_xxxx
# 외곽선 근사화 방법 cv2.CHAIN_APPROX_xxxx
# 검출된 외곽선 좌표 contours, 외곽선 계층정보 hier
contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0
while idx >= 0:
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 외곽선 좌표 contours, 인덱스 idx인 외곽선, 계층정보 hier 포함
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8, hier)
    idx = hier[0, idx, 0]       # hier.shpae=(1,N,4) /// next idx로 바꿈

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
