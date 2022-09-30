# 15658 연산자 끼워넣기
def make(i, now):
    global minV, maxV
    # 연산 횟수 N-1번
    if i == N-1:
        # 연산 완료 후 최소값, 최대값 갱신
        if now < minV:
            minV = now
        if now > maxV:
            maxV = now
    else:
        # 4가지 연산기호에 대해
        for j in range(4):
            # 연산 횟수가 남아있으면
            if op_num[j] > 0:
                op_num[j] -= 1  # 사용 횟수 감소
                # 인덱스 별 연산 기호에 맞는 다음 숫자 만들기
                if j == 0:
                    next = now + nums[i+1]
                elif j == 1:
                    next = now - nums[i+1]
                elif j == 2:
                    next = now * nums[i+1]
                elif j == 3:
                    next = int(now/nums[i+1])
                make(i+1, next)
                op_num[j] += 1  # 다시 올려주기


N = int(input())
nums = list(map(int, input().split()))
op_num = list(map(int, input().split()))
minV = 1000000000
maxV = -1000000000
make(0, nums[0])
print(maxV)
print(minV)
