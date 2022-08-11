T = int(input())
for test_case in range(1, T + 1):
    # N개의 원소, 원소의 합 K
    N, K = map(int, input().split())
    nums = [x for x in range(1, 13)]  # 1~12 집합
    result = 0
    for i in range(1 << 12):
        subset_sum = 0  # 부분집합의 합
        cnt = 0  # 원소개수 셀 변수
        for j in range(12):
            if i & (1 << j):
                subset_sum += nums[j]
                cnt += 1
        # 부분집합의 합이 K이고, 원소개수가 N이면
        if subset_sum == K and cnt == N:
            result += 1
    print(f"#{test_case} {result}")