# 한수의 위치(me_x, me_y), 직사각형의 오른쪽 위 꼭지점(nemo_w, nemo_h) 입력받기
me_x, me_y, nemo_w, nemo_h = map(int, input().split())
# 한수의 위치와 직사각형 경계선까지 최단거리(answer)
answer = min(me_x, nemo_w - me_x, me_y, nemo_h - me_y)
# 결과(answer) 출력하기
print(answer)
