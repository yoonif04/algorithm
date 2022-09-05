T = int(input())
for _ in range(T):
    stack = [0] * 51    # 괄호 문자열 길이 50 이하
    top = -1    # 맨 위 가리킬 변수

    texts = input() # 문자열 정보
    flag = True     # 올바른 괄호 문자열인지 체크
    for text in texts:
        # 여는 괄호라면 스택에 넣기
        if text == "(":
            top += 1
            stack[top] = text
        # 닫는 괄호라면
        else:
            # 스택 top이 여는 괄호인지 확인
            if stack[top] == "(":
                top -= 1
            else:
                flag = False
                break
    if flag == False or top != -1:
        print("NO")
    else:
        print("YES")