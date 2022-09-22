# 풀이1
def move(tx, ty, hx, hy):
    global cnt
    # print("tx, ty, hx, hy", tx, ty, hx, hy)
    # hx, hy가 끝에 도달했으면 종료
    if hx == hy == N-1:
        cnt += 1
        return
    # 그게 아니라면
    else:
        # 가로로 놓여져있으면
        if tx == hx:
            # 오른쪽으로 갈 수 있는지 확인
            if hy + 1 < N and not pipe[hx][hy+1]:
                move(hx, hy, hx, hy + 1)
        # 세로로 놓여져있으면
        elif ty == hy:
            # 아래로 갈 수 있는지 확인
            if hx + 1 < N and not pipe[hx+1][hy]:
                move(hx, hy, hx + 1, hy)
        # 대각선으로 놓여져 있으면
        elif hx - tx == hy - ty == 1:
            # 오른쪽으로 갈 수 있는지
            if hy + 1 < N and not pipe[hx][hy+1]:
                move(hx, hy, hx, hy + 1)
            # 아래로 갈 수 있는지
            if hx + 1 < N and not pipe[hx+1][hy]:
                move(hx, hy, hx + 1, hy)
        # 대각선으로 갈 수 있으면 보내기
        if hy + 1 < N and not pipe[hx][hy+1] and hx + 1 < N and not pipe[hx+1][hy] and not pipe[hx+1][hy+1]:
            move(hx, hy, hx+1, hy+1)


N = int(input())
pipe = [list(map(int, input().split())) for _ in range(N)]
tx, ty = 0, 0
hx, hy = 0, 1
cnt = 0
# 아래 조건문을 안넣으면 90%에서 시간초과됨
if pipe[N-1][N-1] != 1:
    move(tx, ty, hx, hy)
print(cnt)


# 풀이2 - 17069번과 동일
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
