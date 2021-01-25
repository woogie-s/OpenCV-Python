# 3-04. 히스토그램 분석 (2)

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    # 가장 높은 값을 갖는 max값을 미리 찾아내고
    # 미리 설정한 100픽셀(height)을 넘지 않도록 처리
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))    # 100픽셀 넘지않도록!
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

src = cv2.imread('ref/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()
