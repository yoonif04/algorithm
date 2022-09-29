# 5250. 최소비용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = []
    q.append((sx, sy))
    dist = [[INF] * N for _ in range(N)]
    dist[sx][sy] = 0  # 시작점

    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내라면
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0    # 높이 차이
                # 높이 차이가 있으면
                if heights[nx][ny] > heights[x][y]:
                    diff = heights[nx][ny] - heights[x][y]
                # 새로운 좌표의 거리보다 현재 좌표거리에서 높이차이+1이 더 작으면
                if dist[nx][ny] > dist[x][y] + diff + 1:
                    dist[nx][ny] = dist[x][y] + diff + 1
                    q.append((nx, ny))
    return dist[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    INF = 1000000
    print(f"#{tc} {bfs(0, 0)}")
