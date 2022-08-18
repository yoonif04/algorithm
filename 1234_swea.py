# 더할래요. 비밀번호
import sys
sys.stdin = open("input.txt", "r")
T = 10
for tc in range(1, T+1):
    len_pw, pw = input().split()
    li_pw = list(pw)
    stack = [-1]*101  # 스택
    top = 0
    stack[top] = li_pw[0]

    for i in range(1, int(len_pw)):
        # 스택의 top과 다르면 스택에 저장
        if li_pw[i] != stack[top]:
            top += 1
            stack[top] = li_pw[i]
        # 같으면
        else:
            top -= 1
    # 스택에 남은 문자 가져와서 비밀번호 만들기
    password = ""
    for i in range(top+1):
        password += stack[i]
    print(f"#{tc} {password}")