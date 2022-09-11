def calc(x, now_sum):
    global min_val, max_val
    if x == N-1:
        if min_val > now_sum:
            min_val = now_sum
        if max_val < now_sum:
            max_val = now_sum
        return
    else:
        for i in range(4):
            # 해당 연산자가 남아있으면
            if ops[i]:
                # 해당 연산자 개수 줄이고
                ops[i] -= 1
                # 덧셈
                if i == 0:
                    calc(x+1, now_sum+nums[x+1])
                # 뺄셈
                elif i == 1:
                    calc(x+1, now_sum-nums[x+1])
                # 곱셈
                elif i == 2:
                    calc(x+1, now_sum*nums[x+1])
                # 나눗셈일 때
                elif i == 3:
                    # 음수면 양수로 바꾼 후 몫을 구하고 -부호 붙이기
                    if now_sum < 0:
                        calc(x+1, -((-now_sum)//nums[x+1]))
                    else:
                        calc(x+1, now_sum//nums[x+1])
                # 해당 연산자 개수 되돌리기
                ops[i] += 1


N = int(input())
nums = list(map(int, input().split()))
# 연산자의 수, +, -, *, //
ops = list(map(int, input().split()))
min_val = 10**10
max_val = -(10**10)
calc(0, nums[0])
print(max_val)
print(min_val)
