# 5-07. 실전 코딩 - 문서 스캐너

import sys
import numpy as np
import cv2

def drawROI(img, corners):
    cpy = img.copy()

    # 인터페이스 색 지정
    c1 = (192, 192, 255)
    c2 = (128, 128, 255)

    # corners는 nd.array형태 이므로 tuple 형태로 변환해 처리해야함.
    for pt in corners:
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)

    for i, _ in enumerate(corners):
        cv2.line(cpy, tuple(corners[i]), tuple(corners[(i+1)%len(corners)]), c2, 2, cv2.LINE_AA)

    # 선과 원을 그린 부분의 뒤에 배경도 살짝 보이게끔 addweighted
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp

# 파라미터 5개 필수
def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 원 안에 있는 지점을 클릭했을 때
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                dragSrc[i] = True
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:              # 어떤 점을 드래그 하고 있을 경우
                # 현재 점과 이전의 점의 변위를 구해 그만큼 scrQuad에 더해줌
                dx = x - ptOld[0]
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy)

                # 변경사항을 다시 draw
                cpy = drawROI(src, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break


# 입력 이미지 불러오기
src = cv2.imread('ref/scanned.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

# 입력 영상 크기 및 출력 영상 크기
h, w = src.shape[:2]
# 출력할 문서의 가로, 세로 크기 지정
dw = 500
dh = round(dw * 297 / 210)  # A4 용지 크기: 210x297cm

# 모서리 점들의 좌표, 드래그 상태 여부 (반시계방향으로 4개의 지점 위치 초기화)
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)
dragSrc = [False, False, False, False]      # 4개의 점 중 현재 어떤 점을 드래그 하고 있는지 파악하기 위한 bool 변수

# 모서리점, 사각형 그리기
disp = drawROI(src, srcQuad)

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER 키
        break
    elif key == 27:  # ESC 키
        cv2.destroyWindow('img')
        sys.exit()

# 투시 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

# 결과 영상 출력
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()