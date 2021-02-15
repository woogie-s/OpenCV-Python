# 7-08. 다양한 외곽선 함수

import math
import cv2

# Label 생성 함수
def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


def main():
    img = cv2.imread('ref/polygon.bmp', cv2.IMREAD_COLOR)

    if img is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 도형이 더 어두운 형태이므로 inverse 해서 이진화 
    _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for pts in contours:
        if cv2.contourArea(pts) < 400:  #  너무 작으면 무시(노이즈제거)
            continue
        
        # 외곽선 근사화
        # 보통 epsilon(입력곡선과 근사화 곡선 간의 최대거리)에 [외곽선 전체길이]*0.02 를 줌
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

        vtc = len(approx)

        if vtc == 3:
            setLabel(img, pts, 'TRI')
        elif vtc == 4:
            setLabel(img, pts, 'RECT')
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            # 정확한 원이 아니기때문에 1보다 약간 작은 0.85정도로 확인
            if ratio > 0.85:
                setLabel(img, pts, 'CIR')

    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


# 원 판별하기
# 정해진 외곽선 길이에 대한 넓이 비율이 가장 큰 형태가 원
# -> 넓이와 외곽선 길이의 비율을 검사
# 식을 정리하면 4*pi*area/(len*len)이 1에 가까울 수록 원