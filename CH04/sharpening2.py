# 4-04. 샤프닝 - 언샤프 마스크 필터 (2)
# 컬러 영상

import sys
import numpy as np
import cv2

src = cv2.imread('ref/rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# Ycrcb 색상 전환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# Y성분(밝기-0번째)만 이용
# float32로 타입지정 -> GaussianBlur를 이용하면 blr은 입력영상의 타입과 같게 설정이 되는데, 이때 uint8타입을 그대로 GaussianBlur하게 되면 출력영상 blr의 소수점 밑이 다 잘리게 됨.
# 중간 과정에서의 연산 결과를 보존하기 위해 float32 타입으로 변환.
src_f = src_ycrcb[:, :, 0].astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)
# 다시 uint8형으로 변환!!

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
