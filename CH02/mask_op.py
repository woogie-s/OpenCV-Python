# 2-03. 마스크 연산과 ROI

import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('ref/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('ref/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('ref/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

# 검은 배경에 mask부분의 src가 들어감
# dst = cv2.copyTo(src, mask)

# dst영상 안에 mask부분의 src가 들어감
# src, mask, dst는 사이즈가 같아야하고
# src와 dst는 타입이 같아야함. (grayscale - grayscale / color - color)

cv2.copyTo(src, mask, dst)
# dst[mask > 0] = src[mask > 0]
# copyTo와 동일한 기능

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()


# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('ref/cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('ref/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, -1]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출
# copy()를 쓰지 않았기 때문에 src와 픽셀 값 공유

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
