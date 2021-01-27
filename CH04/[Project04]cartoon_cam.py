# 4-07. 실전 코딩 - 카툰 필터 카메라
# 카툰 필터, 스케치 필터

import sys
import numpy as np
import cv2

# 입력 영상의 색상을 단순화시키고, 에지 부분을 검정색으로 강조
def cartoon_filter(img):
    h, w = img.shape[:2]
    # 연산을 효과적으로 하기 위해 영상의 크기를 축소하여 처리를 해준 뒤, 마지막 출력 전에 다시 영상의 크기를 확대.
    img2 = cv2.resize(img, (w//2, h//2))

    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    # 컬러 영상 입력이면 자동으로 그레이스케일 변환해서 검출해줌
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    # bitwise연산을 위해 다시 컬러영상으로 변환

    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    # 값이 급격하게 변하는 느낌을 주기 위해 interpolation 조정

    return dst


# 에지 근방에서 어두운 영역을 검정색으로 설정 (밝은 영역은 흰색)
def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)
    # 255를 곱해서 에지 부분(연산 결과 1보다 작은 부분)만 검게, 나머지는 흰색(255)으로 출력

    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    return dst


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()
