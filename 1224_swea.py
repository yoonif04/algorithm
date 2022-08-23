import sys

sys.stdin = open("input.txt", "r")

# 우선순위
icp = {"+": 1, "*": 2, "(": 3}  # 스택 밖
isp = {"+": 1, "*": 2, "(": 0}  # 스택 안

for tc in range(1, 11):
    n = int(input())  # 문자열의 길이
    exp = list(input())
    stack_num = []  # 숫자 저장할 스택
    stack_op = []  # 연산자 저장할 스택

    # n번 순회하면서 문자열 -> 후위표기식 & 계산
    for i in range(n):
        # 피연산자라면
        if "0" <= exp[i] <= "9":
            stack_num.append(exp[i])
        else:
            # 연산자이고
            # if exp[i] == "+" or exp[i] == "*":
            if exp[i] != ")":
                # 연산자 스택에 다른 연산자가 들어있고, 우선순위가 같거나 높다면
                if stack_op and isp[stack_op[-1]] >= icp[exp[i]]:
                    op = stack_op.pop()
                    num2 = int(stack_num.pop())
                    num1 = int(stack_num.pop())
                    if op == "+":
                        stack_num.append(num1 + num2)
                    else:
                        stack_num.append(num1 * num2)
                stack_op.append(exp[i])
            # # 여는 괄호라면
            # elif exp[i] == "(":
            #     stack_op.append(exp[i])
            # 닫는 괄호라면
            else:
                # 여는 괄호 만날때까지
                while stack_op[-1] != "(":
                    op = stack_op.pop()
                    num2 = int(stack_num.pop())
                    num1 = int(stack_num.pop())
                    if op == "+":
                        stack_num.append(num1 + num2)
                    else:
                        stack_num.append(num1 * num2)
                stack_op.pop()  # 여는 괄호 pop

    while stack_num and stack_op:
        op = stack_op.pop()
        num2 = int(stack_num.pop())
        num1 = int(stack_num.pop())
        if op == "+":
            stack_num.append(num1 + num2)
        else:
            stack_num.append(num1 * num2)

    print(f"#{tc} {stack_num[-1]}")



# 풀이2
# import sys
#
# sys.stdin = open("input.txt", "r")
# 우선순위
icp = {"+": 1, "*": 2, "(": 3}  # 스택 밖
isp = {"+": 1, "*": 2, "(": 0}  # 스택 안

for tc in range(1, 11):
    n = int(input())  # 문자열의 길이
    exp = list(input())
    stack = []
    postfix = ""
    # n번 순회하면서 문자열 -> 후위표기식
    for i in range(n):
        # 피연산자이면 문자열에 더해줌
        if "0" <= exp[i] <= "9":
            postfix += exp[i]
        # 연산자이면
        else:
            # 닫힌 괄호라면 열린괄호 만날때까지 pop
            if exp[i] == ")":
                while stack[-1] != "(":
                    postfix += stack.pop()
                stack.pop()     # 열린괄호 pop
            else:   # 닫힌괄호 아닌 연산자
                # 스택이 비어있지 않고, 우선순위가 더 높다면
                while stack and isp[stack[-1]] >= icp[exp[i]]:
                    postfix += stack.pop()
                stack.append(exp[i])    # 연산자 스택에 추가
    # 스택에 남은 것 -> 후위연산자 문자열에 붙여주기
    while stack:
        postfix += stack.pop()
    # 계산
    result = []
    for x in postfix:
        # 숫자면 스택에 넣기
        if "0" <= x <= "9":
            result.append(int(x))
        else:   # 연산자라면
            num2 = result.pop()
            num1 = result.pop()
            if x == "+":
                result.append(num1 + num2)
            else:
                result.append(num1 * num2)
    print(f"#{tc} {result[0]}")


# 풀이 3
import sys

sys.stdin = open("input.txt", "r")
def calc(op, num1, num2):
    if op == "+":
        return num1 + num2
    else:
        return num1 * num2

# 우선순위
icp = {"+": 1, "*": 2, "(": 3}  # 스택 밖
isp = {"+": 1, "*": 2, "(": 0}  # 스택 안

for tc in range(1, 11):
    n = int(input())  # 문자열의 길이
    exp = list(input())
    stack_num = []  # 숫자 저장할 스택
    stack_op = []  # 연산자 저장할 스택

    # n번 순회하면서 문자열 -> 후위표기식 & 계산
    for i in range(n):
        # 피연산자라면
        if "0" <= exp[i] <= "9":
            stack_num.append(exp[i])
        else:
            # 연산자이고
            # if exp[i] == "+" or exp[i] == "*":
            if exp[i] != ")":
                # 연산자 스택에 다른 연산자가 들어있고, 우선순위가 같거나 높다면
                if stack_op and isp[stack_op[-1]] >= icp[exp[i]]:
                    op = stack_op.pop()
                    num2 = int(stack_num.pop())
                    num1 = int(stack_num.pop())
                    stack_num.append(calc(op, num1, num2))
                stack_op.append(exp[i])
            # # 여는 괄호라면
            # elif exp[i] == "(":
            #     stack_op.append(exp[i])
            # 닫는 괄호라면
            else:
                # 여는 괄호 만날때까지
                while stack_op[-1] != "(":
                    op = stack_op.pop()
                    num2 = int(stack_num.pop())
                    num1 = int(stack_num.pop())
                    stack_num.append(calc(op, num1, num2))
                stack_op.pop()  # 여는 괄호 pop

    while stack_num and stack_op:
        op = stack_op.pop()
        num2 = int(stack_num.pop())
        num1 = int(stack_num.pop())
        stack_num.append(calc(op, num1, num2))

    print(f"#{tc} {stack_num[-1]}")