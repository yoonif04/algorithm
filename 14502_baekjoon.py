from collections import deque
import copy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(li):
    global max_safe
    # list를 받아서 안전영역 세는 함수
    cnt = 0
    for i in range(N):
        for j in range(M):
            if li[i][j] == 0:
                cnt += 1
    if max_safe < cnt:
        max_safe = cnt


def build_wall(cnt):
    # cnt가 3이라면 벽을 3개 다 세운 것 -> bfs탐색
    if cnt == 3:
        bfs()
        return
    # 순회하면서
    for i in range(N):
        for j in range(M):
            # 빈칸이라면 벽을 세우고 다음 함수로
            if graph[i][j] == 0:
                graph[i][j] = 1
                build_wall(cnt+1)
                # 벽 세운것 되돌리기
                graph[i][j] = 0


def bfs():
    q = deque()
    # 벽을 세운 상태의 그래프 복사
    copy_graph = copy.deepcopy(graph)
    # 순회하면서 바이러스가 있다면 큐에 넣기
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 2:
                q.append((i, j))
    # 큐가 비지 않는동안
    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내이고 빈칸(0)이라면
            if 0 <= nx < N and 0 <= ny < M and not copy_graph[nx][ny]:
                copy_graph[nx][ny] = 2  # 바이러스
                q.append((nx, ny))      # 큐에 넣기
    # 안전영역 개수를 셀 함수 호출
    check(copy_graph)


N, M = map(int, input().split())
# 0: 빈칸, 1:벽, 2:바이러스
graph = [list(map(int, input().split())) for _ in range(N)]
# 최대안전영역 수를 구할 변수
max_safe = 0
# 벽세우기 함수 호출
build_wall(0)
print(max_safe)