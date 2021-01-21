# 2-05. 카메라와 동영상 처리하기1(영상 열기)

import sys
import cv2

# 카메라 열기
cap = cv2.VideoCapture(0)   # 카메라 영상 불러오기
# cap = cv2.VideoCapture('ref/video1.mp4')    # 동영상 파일 불러오기

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 크기 세팅
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)
    inversed = ~frame  # 색 반전
    flip = cv2.flip(frame, 1)   # 좌우 대칭 반전

    cv2.imshow('frame', frame)
    cv2.imshow('flip', flip)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27:   # ESC Key
        break

cap.release()
cv2.destroyAllWindows()
