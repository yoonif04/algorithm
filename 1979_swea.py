T = int(input())
for test_case in range(1, T+1):
    # N:가로세로길이,  K:단어길이
    N, K = map(int, input().split())
    # 퍼즐정보 1:흰색부분, 0:검은색부분
    puzzles = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt_row = 0   # 행에서 1의 개수 셀 변수
        cnt_col = 0   # 열에서 1의 개수 셀 변수
        for j in range(N):
            # 행 탐색 -> 0이면 이전까지의 cnt가 K와 같은지 확인
            if puzzles[i][j] == 0:
                if cnt_row == K:
                    result += 1
                cnt_row = 0
            else:  # 1이면 cnt 증가
                cnt_row += 1
            # 열 탐색 -> 0이면 이전까지의 cnt가 K와 같은지 확인
            if puzzles[j][i] == 0:
                if cnt_col == K:
                    result += 1
                cnt_col = 0
            else:
                cnt_col += 1
        # 현재 cnt값이 K와 같다면 -> 끝부분에 K개 공간
        if cnt_row == K:
            result += 1
        if cnt_col == K:
            result += 1
    print(f"#{test_case} {result}")
