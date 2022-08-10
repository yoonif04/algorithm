import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100  # 100행 100열
    nums = [list(map(int, input().split())) for _ in range(N)]
    # 순회하면서 합 구하기
    max_val = 0      # 최댓값 저장 변수
    sum_cross1 = 0   # 왼쪽 대각선 합 저장 변수
    sum_cross2 = 0   # 오른쪽 대각선 합 저장 변수
    for i in range(N):
        sum_row = sum_col = 0   # 행, 열 저장 변수
        for j in range(N):
            sum_row += nums[i][j]
            sum_col += nums[j][i]
            if i == j:          # i,j 같으면 왼쪽 대각선
                sum_cross1 += nums[i][j]
            if j == N-i-1:      # j가 N-i-1이면 오른쪽 대각선
                sum_cross2 += nums[i][j]
        # 행, 열의 합이 최대값인지
        if max_val < sum_row:
            max_val = sum_row
        if max_val < sum_col:
            max_val = sum_col
    # 대각선의 합이 최대값인지
    if max_val < sum_cross1:
        max_val = sum_cross1
    if max_val < sum_cross2:
        max_val = sum_cross2
    print(f"#{tc} {max_val}")