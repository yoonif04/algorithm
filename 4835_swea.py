# List1: 구간합
import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # group_max = 0
    # group_min = 10000*101
    # # 순회하면서 구간합 구하기
    # cur = 0
    # while cur <= N - M:
    #     group_sum = 0
    #     for j in range(cur, cur+M):
    #         group_sum += nums[j]
    #     # 구간합이 가장 작거나 가장 큰지
    #     if group_sum < group_min:
    #         group_min = group_sum
    #     if group_sum > group_max:
    #         group_max = group_sum
    #     cur += 1

    # 풀이2
    group_sum = 0
    for i in range(M):  # M개 더해서 초기 그룹합
        group_sum += nums[i]
    group_max = group_min = group_sum

    # M부터 N-1까지 순회
    for i in range(M, N):
        # 그룹합에서 i번째 더해주고 i-M번째 빼준다
        group_sum += (nums[i] - nums[i-M])
        # 구간합이 가장 작거나 가장 큰지
        if group_sum < group_min:
            group_min = group_sum
        if group_sum > group_max:
            group_max = group_sum

    print(f"#{test_case} {group_max-group_min}")