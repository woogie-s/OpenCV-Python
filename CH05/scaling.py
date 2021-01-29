# 5-02. 영상의 확대와 축소
 
import sys
import numpy as np
import cv2


src = cv2.imread('ref/rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

# 결과영상 크기 dsize 또는 x와 y방향 스케일 비율 fx, fy 중 하나는 입력해주어야 함.
# dsize가 (0, 0)이면 fx와 fy값을 이용해 결정
dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

# 영상의 대칭은 크기변환과 관련 있음. 좌우대칭은 -1배 확대하고 대칭이동한 결과
# 1(좌우대칭), 0(상하대칭), -1(좌우&상하 대칭)
dst5 = cv2.flip(src, 1)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()

