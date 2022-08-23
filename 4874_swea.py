# 4874. Forth
T = int(input())
for tc in range(1, T+1):
    exp = list(input().split())
    size = 300
    stack = [0]*size
    top = -1
    result = 'error'
    for i in range(len(exp)):
        # 피연산자이면 스택에 넣기
        if exp[i].isnumeric():
            top += 1
            stack[top] = exp[i]
        # 연산자라면
        elif exp[i] == "+" or exp[i] == "-" or exp[i] == "*" or exp[i] == "/":
            op = exp[i]
            # 스택 위 두개가 숫자여야 한다.
            if top >= 1:
                num2 = int(stack[top])
                top -= 1
                num1 = int(stack[top])
                if op == "+":
                    stack[top] = num1 + num2
                elif op == "-":
                    stack[top] = num1 - num2
                elif op == "*":
                    stack[top] = num1 * num2
                elif op == "/":
                    stack[top] = num1 // num2  # 정수로
            # 그게 아니라면 에러
            else:
                result = 'error'
                break
        else:  # .이라면 결과 출력
            result = stack[top]
    if top == 0 and result != 'error':
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} error")