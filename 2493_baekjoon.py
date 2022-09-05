N = int(input())
nums = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N):
    # 스택 빌 때까지
    while stack:
        # 스택의 마지막 값과 비교
        # 더 크다면 결과에 인덱스 + 1 넣기
        if stack[-1][1] > nums[i]:
            result[i] = stack[-1][0] + 1
            break
        # 작다면 제거
        else:
            stack.pop()
    # 스택에 해당번호 인덱스와 값 넣기
    stack.append([i, nums[i]])

print(*result)