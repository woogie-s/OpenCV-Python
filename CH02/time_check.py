# 2-10. 연산 시간 측정 방법

import sys
import time
import numpy as np
import cv2

img = cv2.imread('ref/hongkong.jpg')

tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()        # time 함수 사용해도 무방

edge = cv2.Canny(img, 50, 150)
# 몇번씩 수행해서 평균적인 시간을 구하는 것이 좋음

tm.stop()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))
