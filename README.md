# OpenCV-Python

OpenCV에 대해 공부하고, Python을 활용한 OpenCV 활용법에 대해 공부한 것을 기록하는 공간입니다.

<a href="https://fastcampus.co.kr/">FastCampus</a>의 <OpenCV를 활용한 컴퓨터비전과 딥러닝 올인원 패키지 Online> 강의를 통해 실습한 내용을 기록하고 정리하였습니다.

___

## < Chapter 01 > OpenCV-Python 시작하기
1. 전체 코스와 컴퓨터 비전 소개
2. 영상의 구조와 표현
3. OpenCV 소개와 설치
4. VS Code 설치와 개발 환경 설정
5. 영상 파일 불러와서 출력하기
6. OpenCV 주요 함수 설명
7. <a href="/CH01/matplot.py">Matplotlib 사용하여 영상 출력하기</a>
8. <a href="/CH01/[Project01]SlideShow.py">실전 코딩 - 이미지 슬라이드쇼</a>

<br>

## < Chapter 02 > OpenCV-Python 기초 사용법
1. <a href="/CH02/img_info.py">영상의 속성과 픽셀 값 처리</a>
2. <a href="/CH02/img_ops.py">영상의 생성, 복사, 부분 영상 추출</a>
3. <a href="/CH02/mask_op.py">마스크 연산과 ROI</a>
4. <a href="/CH02/drawing.py">OpenCV 그리기 함수</a>
5. <a href="/CH02/camera_in.py">카메라와 동영상 처리하기 1 (영상 열기)</a>
6. <a href="/CH02/video_out.py">카메라와 동영상 처리하기 2 (영상 저장)</a>
7. <a href="/CH02/keyboard.py">키보드 이벤트 처리하기</a>
8. <a href="/CH02/mouse.py">마우스 이벤트 처리하기</a>
9. <a href="/CH02/trackbar.py">트랙바 사용하기</a>
10. <a href="/CH02/time_check.py">연산 시간 측정 방법</a>
11. <a href="/CH02/[Project02]video_effect.py">실전 코딩 - 동영상 전환 이펙트</a>

<br>

## < Chapter 03 > 기본적인 영상 처리 기법
1. <a href="/CH03/brightness.py">영상의 밝기 조절</a>
2. <a href="/CH03/arithmetic.py">영상의 산술 및 논리 연산</a>
3. <a href="/CH03/color.py">컬러 영상 처리와 색 공간</a>
4. 히스토그램 분석 &nbsp;<a href="/CH03/histogram1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH03/histogram2.py">( 2 )</a>
5. 영상의 명암비 조절 &nbsp;<a href="/CH03/contrast1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH03/contrast2.py">( 2 )</a>
6. <a href="/CH03/equalize.py">히스토그램 평활화</a>
7. 특정 색상 영역 추출하기 &nbsp;<a href="/CH03/inrange1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH03/inrange2.py">( 2 )</a>
8. 히스토그램 역투영 &nbsp;<a href="/CH03/backproj1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH03/backproj2.py">( 2 )</a>
9. 실전 코딩 - 크로마키 합성 &nbsp;<a href="/CH03/[Project03]chroma_key1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH03/[Project03]chroma_key2.py">( 2 )</a>

<br>

## < Chapter 04 > 필터링
1. 필터링 이해하기
2. 블러링 (1) - 평균값 필터 &nbsp;<a href="/CH04/blurring1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH04/blurring2.py">( 2 )</a>
3. 블러링 (2) - 가우시안 필터 &nbsp;<a href="/CH04/gaussian1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH04/gaussian2.py">( 2 )</a>
4. 샤프닝 - 언샤프 마스크 필터 &nbsp;<a href="/CH04/sharpening1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH04/sharpening2.py">( 2 )</a>
5. <a href="/CH04/median.py">잡음 제거 (1) - 미디언 필터</a>
6. <a href="/CH04/bilateral.py">잡음 제거 (2) - 양방향 필터</a>
7. <a href="/CH04/[Project04]cartoon_cam.py">실전 코딩 - 카툰 필터 카메라</a>

<br>

## < Chapter 05 > 기하학적 변환
1. 영상의 <a href="/CH05/translate.py">이동 변환</a>과 <a href="/CH05/shear.py">전단 변환</a>
2. <a href="/CH05/scaling.py">영상의 확대와 축소</a>
3. <a href="/CH05/pyramid.py">이미지 피라미드</a>
4. 영상의 회전 &nbsp;<a href="/CH05/rotation1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH05/rotation2.py">( 2 )</a>
5. <a href="/CH05/perspective.py">어파인 변환과 투시 변환</a>
6. <a href="/CH05/remap.py">리매핑</a>
7. <a href="/CH05/[Project05]docuscan.py">실전 코딩 - 문서 스캐너</a>

<br>

## < Chapter 06 > 영상의 특징 추출
1. <a href="/CH06/sobel.py">영상의 미분과 소베 필터</a>
2. <a href="/CH06/sobel_edge.py">그래디언트와 에지 검출</a>
3. <a href="/CH06/canny.py">캐니 에지 검출</a>
4. <a href="/CH06/hough_lines.py">허프 변환 직선 검출</a>
5. <a href="/CH06/hough_circles.py">허프 원 변환 원 검출</a>
6. <a href="/CH06/[Project06]coin_count.py">실전 코딩 - 동전 카운터</a>

<br>

## < Chapter 07 > 이진 영상 처리
1. 영상의 이진화 &nbsp;<a href="/CH07/threshold1.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH07/threshold2.py">( 2 )</a>
2. <a href="/CH07/otsu.py">자동 이진화 Otsu 방법</a>
3. 지역 이진화 &nbsp;<a href="/CH07/local_th.py">( 1 )</a> &nbsp;/&nbsp; <a href="/CH07/adaptive_th.py">( 2 )</a>
4. 모폴로지(1) - <a href="/CH07/morphology.py">침식과 팽창</a>
