icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

exp = list(input())
postfix = ''
# 연산자 담을 스택
stack = [0] * len(exp)
top = -1

for e in exp:
    # 문자라면 붙여주기
    if e.isalpha():
        postfix += e
    # 연산자라면
    else:
        # 닫는 괄호일 때
        if e == ")":
            while True:
                # 여는 괄호만나면 pop하고 종료
                if stack[top] == "(":
                    top -= 1
                    break
                # 그게 아니라면 계속 연산자 꺼내기
                else:
                    postfix += stack[top]
                    top -= 1
        # 닫는 괄호를 제외한 연산자라면
        else:
            # 스택에 값이 존재하다면 우선순위 비교하여 크거나 같은 연산자 꺼내기
            while top > -1 and isp[stack[top]] >= icp[e]:
                postfix += stack[top]
                top -= 1
            # 스택에 연산자 넣기
            top += 1
            stack[top] = e

while top > -1:
    postfix += stack[top]
    top -= 1
print(postfix)