# 2-08. 마우스 이벤트 처리하기

import sys
import numpy as np
import cv2

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)   
            # 빠르게 움직이면 끊기는 현상 발생 -> line 함수를 이용
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)    # 'image'라는 창이 만들어진 이후에 실행 가능

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
