T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0  # 구조물의 최대 길이 담을 변수

    for i in range(N):
        cnt_row = cnt_col = 0
        for j in range(M):
            # 행 탐색 - 1이면 cnt 증가(이후 max인지 판단후갱신), 0이면 0 초기화
            if nums[i][j] == 1:
                cnt_row += 1
            else:
                cnt_row = 0
            # 열 탐색
            if nums[j][i] == 1:
                cnt_col += 1
            else:
                cnt_col = 0
            # 최대값 갱신
            if max_val < cnt_row:
                max_val = cnt_row
            if max_val < cnt_col:
                max_val = cnt_col

    print(f"#{test_case} {max_val}")