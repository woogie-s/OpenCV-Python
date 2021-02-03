# 6-03. 캐니 에지 검출
# 가우시안 필터링(optional) > 그래디언트 계산(크기&방향) 
# > 비최대 억제 > 이중 임계값을 이용한 히스테리시스 에지 트래킹

import sys
import numpy as np
import cv2

src = cv2.imread('ref/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 입력영상 src, low 임계값 50, high 임계값 150
# L2gradient 기본값 False(L1 norm 사용), True 지정시(L2 norm)
dst = cv2.Canny(src, 50, 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 비최대 억제 : 그래디언트 방향에 위치한 두개의 픽셀을 조사해 국지적 최대를 검사. 한 픽셀의 에지를 검출하는 과정

# 히스테리시스 에지 트래킹 : 두개의 임계값 사용
# T_high 보다 크면 강한 에지, T_low <= x < T_high : 약한에지
# 약한 에지 중 강한 에지와 연결되는 픽셀만 최종적으로 에지로 판단