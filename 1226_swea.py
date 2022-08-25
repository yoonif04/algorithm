import sys
sys.stdin = open("input.txt", "r")
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    visited[i][j] = 1
    q = [(i, j)]  # 시작점 넣기
    while q:
        i, j = q.pop(0)
        if i == j == 13:    # 도착점이면 함수 종료
            return
        # 4방향 탐색
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            # 범위 내이고, 벽(1)이 아니고, 방문한적이 없다면
            if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] != 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


for _ in range(1, 11):
    tc = int(input())
    N = 16  # 가로,세로 길이
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * 16 for _ in range(16)]
    bfs(1, 1)
    print(f"#{tc} {visited[13][13]}")
