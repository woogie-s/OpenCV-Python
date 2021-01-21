# 2-09. 트랙바 사용하기

import numpy as np
import cv2

def on_level_change(pos):
    global img
    value = pos * 16
    if value >= 255:
        value = 255

    # if 조건 대신 이렇게도 사용 가능
    # value = np.clip(value, 0, 255)

    img[:] = value
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)    # 트랙바 초기값 0, 최댓값 16
# 'image' 창이 생성된 이후에 실행!

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
