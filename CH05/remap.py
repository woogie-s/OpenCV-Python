# 5-06. 리매핑

import sys
import numpy as np
import cv2

src = cv2.imread('ref/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)

# map1 : 결과영상의 (x, y)좌표가 참조할 입력영상의 x좌표
# map2 : 결과영상의 (x, y)좌표가 참조할 입력영상의 y좌표
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# map2, map1 = np.indices((3, 3))
# map2 = [[0, 0, 0],        map1 = [[0, 1, 2],
#         [1, 1, 1],                [0, 1, 2],
#         [2, 2, 2]]                [0, 1, 2]]
