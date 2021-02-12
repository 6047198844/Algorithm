# 출처 https://programmers.co.kr/learn/courses/30/lessons/62048
# input W : 가로 길이, H : 세로 길이 (1억 이하의 자연수)
# output 멀쩡한 사각형의 갯수
# 가로 길이 W, 세로 길이 H인 사각형을 대각선으로 자를 때, 가로 세로가 1cm인 사각형이 몇개인가?

import math
def solution(w,h):
    answer = 0
    all = w * h
    x, y = w, h # x는 최대 공약수
    while y:
        x, y = y, x % y
    # 수학을 이용한 간편한 풀이
    # answer = (w//x - 1) + (h//x - 1) + 1
    # return all - answer * x
    if w == h:
        return all - w
    elif h > w:
        for i in range(w // x):
            answer += math.ceil(h*(i+1)/w) - int(h * i / w)
    else:
        for i in range(h // x):
            answer += math.ceil(w*(i + 1)/h) - int(w * i / h)

    return all - answer * x

print(solution(8, 12) == 80, solution(8, 12))
