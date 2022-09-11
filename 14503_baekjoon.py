from collections import deque

# dx, dy 이동 - 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy, sd):
    visited = [[0] * M for _ in range(N)]  # 청소 여부 나타내기
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1  # 시작점 청소
    clean = 1  # 청소한 개수
    d = sd  # 시작 방향
    while q:
        x, y = q.popleft()
        for _ in range(4):
            # 왼쪽 방향 탐색
            d = (d - 1 + 4) % 4
            nx, ny = x + dx[d], y + dy[d]
            # 범위내이고, 벽이 아니고, 청소 안했으면 청소
            if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1     # 청소했다고 표시
                clean += 1  # 청소한 개수 늘리기
                q.append((nx, ny))
                break
        else:
            # 네 방향 모두 청소되어있거나 벽인 경우 후진 가능한지
            # 후진 시의 좌표
            nx, ny = x - dx[d], y - dy[d]
            # 범위 내이고, 벽이 아니라면 후진 가능
            if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny]:
                q.append((nx, ny))  # 후진할 칸을 큐에 넣기
            # 그게 아니라면 탐색 종료
            else:
                return clean


# NxM
N, M = map(int, input().split())
# 시작 x, y, 시작방향
sx, sy, sd = map(int, input().split())
# 지도 정보
graph = [list(map(int, input().split())) for _ in range(N)]
print(bfs(sx, sy, sd))
