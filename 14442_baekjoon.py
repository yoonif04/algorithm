from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque()
    # 시작점 sx, sy, 부순횟수, 거리
    q.append([sx, sy, 0, 1])
    visited[0][sx][sy] = 1

    while q:
        x, y, c, dist = q.popleft()
        # 마지막 위치에 도달했다면 거리 반환
        if x == N - 1 and y == M - 1:
            return dist
        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내이고
            if 0 <= nx < N and 0 <= ny < M:
                # 이동가능하고 방문하지 않았다면
                if graph[nx][ny] == 0 and not visited[c][nx][ny]:
                    visited[c][nx][ny] = 1  # 방문처리
                    q.append([nx, ny, c, dist + 1])
                    # 이동불가능하고 벽을 부술 수 있다면(c가 K보다 작고 c+1 방문하지 않은 상태)
                elif graph[nx][ny] == 1 and c < K and not visited[c+1][nx][ny]:
                    visited[c + 1][nx][ny] = 1
                    q.append([nx, ny, c + 1, dist + 1])
    return -1


N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
# 방문여부 -> K차원
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
print(bfs(0, 0))

# 시간초과 -> 마지막 elif에서 visited조건 추가하여 중복 방문 막아서 해결
import sys
from collections import deque

input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy, b_cnt):
    # 시작위치 sx,sy, 벽을 부순 횟수 b_cnt
    q = deque()
    q.append((sx, sy, b_cnt))
    # 시작 칸의 거리 1
    dist[sx][sy][b_cnt] = 1

    while q:
        x, y, c = q.popleft()
        # 마지막 위치에 도달했다면 거리 반환
        if x == N - 1 and y == M - 1:
            return dist[x][y][c]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내이고 방문 안했다면
            if 0 <= nx < N and 0 <= ny < M and not dist[nx][ny][c]:
                # 이동가능
                if graph[nx][ny] == 0:
                    # 이전 좌표에서 1 추가 후 큐에 넣기
                    dist[nx][ny][c] = dist[x][y][c] + 1
                    q.append((nx, ny, c))
                # 이동 불가능하고 벽을 부술 수 있다면
                elif graph[nx][ny] == 1 and c + 1 <= K and not dist[nx][ny][c+1]:
                    dist[nx][ny][c + 1] = dist[x][y][c] + 1
                    q.append((nx, ny, c + 1))
    return -1


N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# 벽 부시기 -> 0개~K개 -> K+1개
dist = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, 0))
