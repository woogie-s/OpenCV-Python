# 1. OpenCV-Python 시작하기

## OpenCV 주요함수 설명

OpenCV API 최신 도움말 : <http://docs.opencv.org/master/>
<hr><br>
1. 영상파일 불러오기

```python
import cv2

src = cv2.imread(filename , flags=None)
```
- filename : 불러올 영상 파일 이름
- flags : 영상 파일 불러올 때 옵션
    | | |
    |---|---|
    | cv2.IMREAD_COLOR | BGR컬러 영상으로 읽기(default) |
    | cv2.IMREAD_GRAYSCALE | GRAYSCALE 영상으로 읽기 |
    | cv2.IMREAD_UNCHANGED | 영상 파일 속성 그대로 읽기 |
- src : 불러온 영상 데이터 저장 (numpy.ndarray 형태)

<hr><br>   
2. 영상파일 저장하기

```python
cv2.write(filename, img, params=None)
```
- filename : 저장할 영상 파일 이름
- img : 저장할 영상 데이터 (numpy.ndarray 형태)
- params : 파일 저장 옵션 지정 ( [저장할 옵션, 정수] 형태)
- 저장에 성공하면 Return True, 실패 시 False

<hr><br>
3. 새 창 띄우기

```python
cv2.namedWindow(winname, flags=None)
```
- winnmae : 새로 띄우는 창의 고유 이름 (문자열 형태)
- flags : 창 속성 지정 플래그
    | | |
    |---|---|
    | cv2.WINDOW_NORMAL | 영상 크기를 창 크기에 맞게 |
    | cv2.WINDOW_AUTOSIZE | 창 크기를 영상 크기에 맞게(default) |

<hr><br>
4. 창 닫기

```python
cv2.destroyWindow(winname)
cv2.destroyAllWindows()
```
- winname : 닫으려는 창 이름
- 참고 사항  
    - destroyAllWindows는 열려 있는 모든 창을 닫는 것이고, destroyWindow는 지정한 창만 닫는 것.
    - 프로그램 종료 시, 열려 있는 모든 창이 자동으로 닫힘.

<hr><br>
5. 창 위치 이동 및 창 크기 변경

```python
cv2.moveWindow(winname, x, y)
cv2.resizeWindow(winname, width, height)
```
- winname : 창 이름
- x, y : 이동할 좌표
- width, height : 변경할 창의 가로, 세로 크기
    - 이때, 창 크기 변경은 cv2.WINDOW_NORMAL 속성으로 생성해야 가능하다.

<hr><br>
6. 영상 출력하기 및 키보드 입력대기

```python
cv2.imshow(winname, mat)
cv2.waitKey(delay=None)
```
- winname : 영상 출력할 창 이름
- mat : 출력할 영상 데이터 (numpy.ndarray 형태)
- delay : ms단위의 대기 시간. delay<=0 이면 무한히 기다리며 기본값은 0.
- imshow 호출 후 waitKey를 작성해야 실제로 영상이 화면에 나타나며, waitKey 또한 OpenCV창이 하나라도 존재해야 작동한다.
- waitKey 에서 받은 키보드 입력은 아스키코드로 받으며, ord()함수를 이용해 입력받은 키를 확인할 수 있다.

<hr><br>

## Matplotlib 사용하여 영상 출력하기
Matplotlib 라이브러리는 함수 그래프, 차트, 히스토그램 등 다양한 그리기 기능을 제공하는 python 패키지이다.

> pip install matplotlib

**컬러 영상**의 색상 정보 순서가 RGB 순서여야 하기 때문에, cv2.cvtColor() 함수를 이용해 색상 정보의 순서를 바꾸어야 한다.  
**그레이스케일 영상**의 경우 plt.imshow() 함수에서 cmap='gray'로 지정한다.

```python
import matplotlib.pyplot as plt

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
```

Matplotlib을 이용해 창 하나에 여러 개의 이미지도 출력 가능하다.  
방법은 다음과 같다.

```python
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
```