# 2-07. 키보드 이벤트 처리하기

import sys
import numpy as np
import cv2


img = cv2.imread('ref/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode = cv2.waitKey()     # 키보드 입력 한번만 받아서 처리할수 있도록
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()
