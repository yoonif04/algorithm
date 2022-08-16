T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    max_val = 0
    cnt = 0
    for num in nums:
        if num == 1:
           cnt += 1
           if max_val < cnt:
               max_val = cnt
        else:
            cnt = 0
    print(f"#{test_case} {max_val}")