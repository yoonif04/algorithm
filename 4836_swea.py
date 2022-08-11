T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 칠할 영역 개수
    paper = [[0] * 10 for _ in range(10)]  # 색칠할 영역
    cnt = 0  # 보라색 영역 개수 셀 변수
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if paper[i][j] == 0:
                    paper[i][j] = color
                elif paper[i][j] != color:
                    cnt += 1
    print(f"#{test_case} {cnt}")