# 4866. 괄호 검사
T = int(input())
for tc in range(1, T + 1):
    text = input()
    size = 1000
    stack = [0] * size
    s_idx = -1  # 스택의 현재 인덱스 위치
    answer = 1  # 정상여부 나타낼 변수 1:정상, 0:비정상

    # 순회
    for word in text:
        # 여는 괄호라면 스택에 넣기
        if word == "(" or word == "{":
            s_idx += 1
            stack[s_idx] = word
        # 닫는 괄호 ")"라면
        elif word == ")":
            # 스택의 맨 위에 "("가 있으면 정상 -> pop
            if stack[s_idx] == "(":
                s_idx -= 1
            else:  # 아니면 잘못된 경우
                answer = 0
        # 닫는 괄호 "}"라면
        elif word == "}":
            # 스택의 맨 위에 "{"가 있으면 정상 -> pop
            if stack[s_idx] == "{":
                s_idx -= 1
            else:  # 아니면 잘못된 경우
                answer = 0
    # 스택의 길이가 0이 아니면(인덱스가 -1을 가리키지 않으면) 잘못된 경우
    if s_idx != -1:
        answer = 0
    print(f"#{tc} {answer}")
