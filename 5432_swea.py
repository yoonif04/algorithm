T = int(input())
for tc in range(1, T+1):
    sticks = input()
    stack = 0
    result = 0  # 결과 개수 저장할 변수

    #순회
    for i in range(len(sticks)):
        if sticks[i] == '(':   # 여는 괄호라면
            stack += 1   # 스택에 1 추가
        else:   # 닫는 괄호라면
            stack -= 1   # 스택 1 감소
            # 이전이 여는 괄호라면
            if sticks[i-1] == '(':
                result += stack   # 스택값만큼 추가
            else:
                result += 1

    print(f"#{tc} {result}")