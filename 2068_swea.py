T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    max_val = -1
    for num in nums:
        if max_val < num:
            max_val = num
    print(f"#{test_case} {max_val}")