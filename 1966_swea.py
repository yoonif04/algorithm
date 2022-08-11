T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if nums[minIdx] > nums[j]:
                minIdx = j
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
    print(f"#{test_case}", end=" ")
    print(*nums)