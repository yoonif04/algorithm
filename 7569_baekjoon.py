from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    day = 0
    q = deque()
    # 익은 토마토 구해서 큐에 넣기
    for h in range(H):  # 상자 번호
        for r in range(N):  # 행
            for c in range(M):  # 열
                if tomatoes[h][r][c] == 1:
                    q.append((h, r, c))
                    visited[h][r][c] = 1
    # 큐가 비어있지 않으면
    while q:
        # 큐의 길이만큼 진행: 큐의 길이만큼 -> 하루에 가능한 양
        for _ in range(len(q)):
            h, i, j = q.popleft()
            # 상하좌우의 토마토
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                # 범위 내이고 토마토가 들어있지 않은 상태가 아니며, 방문하지 않은 경우
                if 0 <= ni < N and 0 <= nj < M and tomatoes[h][ni][nj] != -1 and not visited[h][ni][nj]:
                    tomatoes[h][ni][nj] = 1     # 토마토 익었다고 바꿔줌
                    visited[h][ni][nj] = 1      # 방문
                    q.append((h, ni, nj))       # 큐에 넣기
            # 위,아래 상자의 토마토
            up = h - 1
            down = h + 1
            # 위 상자 존재, 토마토가 들어있지 않은 상태가 아니며, 방문하지 않은 경우
            if up >= 0 and tomatoes[up][i][j] != -1 and not visited[up][i][j]:
                tomatoes[up][i][j] = 1      # 토마토 익었다고 바꿔줌
                visited[up][i][j] = 1       # 방문
                q.append((up, i, j))        # 큐에 넣기
            # 아래 상자 존재, 토마토가 들어있지 않은 상태가 아니며, 방문하지 않은 경우
            if down < H and tomatoes[down][i][j] != -1 and not visited[down][i][j]:
                tomatoes[down][i][j] = 1    # 토마토 익었다고 바꿔줌
                visited[down][i][j] = 1     # 방문
                q.append((down, i, j))      # 큐에 넣기
        day += 1    # 하루 지났음

    # 익지 않은 토마토가 있는지 확인
    for h in range(H):
        for r in range(N):
            for c in range(M):
                # 0이면 익지 않은 토마토 존재 -> -1 리턴
                if not tomatoes[h][r][c]:
                    return -1
    # 여기까지 도달한 경우 익지 않은 토마토 없음 -> day 반환
    return day - 1


# M:상자 가로, N:상자 세로, H:상자 수
M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
print(bfs())
