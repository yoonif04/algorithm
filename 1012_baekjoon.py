di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    visited[i][j] = 1
    q = [(i,j)]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<=ni<N and 0<=nj<M and graph[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    # M:가로길이, N:세로길이, K:배추위치개수
    M, N, K = map(int, input().split())

    graph = [[0]*(M+1) for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    visited = [[0]*M for _ in range(N)]
    cnt = 0     # 지렁이 수
    for i in range(N):
        for j in range(M):
            # 배추 심어져 있고 방문 안했으면 bfs실행
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)