# 2-04. OpenCV 그리기 함수

import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)      # (50, 50) ~ (200, 50)에 (0,0,255)색상, 두께5의 직선
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))        # (50, 60) ~ (150, 160)에 (0, 0, 128)색상, 두께1(기본값)의 직선


cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)     # (기준점 x, y, width, height), 두께 2
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)      # 좌상단 point, 우하단point, -1(내부 채우기)

cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)     # (300, 100) 점에서 30 반지름, (255, 255, 0)색으로 -1(내부 채우기), Anti-Aliasing
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)       # 다각형 그리기
# pts를 list형태로 입력해야함.

text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)       #(50, 350)은 문자열 출력할 좌측 하단 좌표

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

