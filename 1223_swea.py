import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    n = int(input())    # 식의 길이(문자 갯수)
    infix = input()     # 중위표기식을 문자열로 입력 받기

    stack1 = [0] * n     # 스택의 길이는 최대 n
    stack2 = [0] * n     # 숫자 담을 스택
    top1 = -1
    top2 = -1

    # 연산자의 우선순위
    icp = {"+":1, "-":1, "/":2, "*":2}

    # 중위연산식을 순회하면서 후위연산식으로 바꾸기
    for i in range(n):
        # i번째 문자를 하나 떼와서
        if "0" <= infix[i] <= "9":  #피연산자, 숫자인경우
            top2 += 1
            stack2[top2] = infix[i]
        else:
            # 연산자인 경우
            if top1 > -1 and icp[stack1[top1]] >= icp[infix[i]]:
                op = stack1[top1]
                top1 -= 1
                num2 = int(stack2[top2])
                top2 -= 1
                num1 = int(stack2[top2])
                if op == "+":
                    stack2[top2] = num1 + num2
                elif op == "-":
                    stack2[top2] = num1 - num2
                elif op == "*":
                    stack2[top2] = num1 * num2
                elif op == "/":
                    stack2[top2] = num1 / num2
            top1 += 1
            stack1[top1] = infix[i]


    while top1 > -1 and top2 > -1:
        op = stack1[top1]
        top1 -= 1
        num2 = int(stack2[top2])
        top2 -= 1
        num1 = int(stack2[top2])
        if op == "+":
            stack2[top2] = num1 + num2
        elif op == "-":
            stack2[top2] = num1 - num2
        elif op == "*":
            stack2[top2] = num1 * num2
        elif op == "/":
            stack2[top2] = num1 / num2
    print(f"#{tc} {stack2[top2]}")