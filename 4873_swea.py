# 4873. 반복문자 지우기
import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    text = input()          # 입력받을 문자
    size = 1001             # 문자의 길이
    stack = [0] * size      # 스택 만들기
    top = 0                 # 스택 위치 나타낼 변수
    stack[top] = text[0]    # 첫 문자열을 스택에 넣고 시작
    # 하나씩 꺼내서
    for i in range(1, len(text)):
        word = text[i]      # i번째 문자
        top_word = stack[top]   # 스택의 맨 위 문자
        # 스택과 같은 문자라면
        if top_word == word:
            top -= 1        # pop
        else:   # 스택과 다른 문자라면 push
            top += 1
            stack[top] = word
    print(f"#{tc} {top+1}")