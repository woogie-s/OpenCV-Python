# 8-03. 템플릿 매칭 (1)
# TM_CCOEFF_NORMED 을 사용했기 때문에 밝기 변화나 노이즈에는 상관없으나
# 회전변환, 크기변환된 영상에서는 템플릿 매칭이 어려움.

import sys
import numpy as np
import cv2

# 입력 영상 & 템플릿 영상 불러오기
src = cv2.imread('ref/circuit.bmp', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('ref/crystal.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()

# 입력 영상 src 밝기 50증가, 가우시안 잡음(sigma=10) 추가
noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10)
src = cv2.add(src, noise, dtype=cv2.CV_8UC3)

# res - 템플릿 매칭 & res_norm - 결과 분석(grayscale 영상으로 출력하기 위해)
res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED)
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# min값, max값, min위치, max위치
_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)
print('maxloc:', maxloc)

# 매칭 결과를 빨간색 사각형으로 표시
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

if maxv > 0.7:
    th, tw = templ.shape[:2]
    cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

# 결과 영상 화면 출력
cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
