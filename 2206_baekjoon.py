import sys
from collections import deque


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        # 마지막 좌표에 도착했으면 경로길이 반환
        if x == N - 1 and y == M - 1:
            return visited[x][y][w]
        # 상하좌우 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 새 좌표가 범위내에 있으면
            if 0 <= nx < N and 0 <= ny < M:
                # 이동할수있고 방문 안했다면
                if not graph[nx][ny] and not visited[nx][ny][w]:
                    # 이전 좌표에서 1 추가
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
                # 이동할수 없고 벽을 아직 뚫지 않았다면
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])
    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs())

# 시간 초과
from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global min_move
    # copy_graph = copy.deepcopy(graph)
    copy_graph = graph[:]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))  # 0,0에서 출발
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위내이고 방문 가능한데(0인데) 방문 안했으면
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not copy_graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    # 마지막 값
    move = visited[N - 1][M - 1]
    if 1 < move < min_move:
        min_move = move


def build_wall(cnt):
    if cnt == 1:
        bfs()
        return
    # 순회하면서
    for i in range(N):
        for j in range(M):
            # 벽이 있으면
            if graph[i][j] == 1:
                # 0으로 바꾸고 다음 함수 호출
                graph[i][j] = 0
                build_wall(cnt + 1)
                graph[i][j] = 1  # 되돌리기


N, M = map(int, input().split())
# 0:이동가능, 1:벽
graph = [list(map(int, input().rstrip())) for _ in range(N)]
min_move = 1000 * 1001
build_wall(0)
if min_move == 1000 * 1001:
    print(-1)
else:
    print(min_move)
