N = int(input())
pipe = [list(map(int, input().split())) for _ in range(N)]
# 0:가로, 1:세로, 2:대각선
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1     # 첫 시작 위치

# dp 위해서는 윗행을 사용해야함 -> 첫 행을 먼저 초기화
# 맨 첫줄은 가로만
for i in range(2, N):
    if pipe[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

# 두번째 줄부터
for i in range(1, N):
    # 파이프가 (0,0), (1,0)에 놓여있으므로 -> 3번째부터
    for j in range(2, N):
        # 해당자리, 위쪽, 왼쪽이 0이면
        # 대각선방향에서부터, 가로/세로/대각선에서
        if pipe[i][j] == 0 and pipe[i-1][j] == 0 and pipe[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

        if pipe[i][j] == 0:
            # 가로 - 왼쪽에서부터, 가로/대각선에서만
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로 - 위에서부터, 세로/대각선에서만
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

answer = sum([dp[x][N-1][N-1] for x in range(3)])
print(answer)