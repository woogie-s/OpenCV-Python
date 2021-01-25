# 3-03. 컬러 영상 처리와 색 공간

import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('ref/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색을 각각 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)

#b_plane = src[:, :, 0]
#g_plane = src[:, :, 1]
#r_plane = src[:, :, 2]

cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.waitKey()

# HSV 색 공간 
# src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h_plane, s_plane, v_plane = cv2.split(src_hsv)

# cv2.imshow('H_plane', h_plane)
# cv2.imshow('S_plane', s_plane)
# cv2.imshow('V_plane', v_plane)

cv2.destroyAllWindows()
