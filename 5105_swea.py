# 5105. 미로의 거리
# 이동: 상,하,좌,우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    # 방문여부와 이동칸수를 저장
    visited = [[0] * N for _ in range(N)]
    q = [(si, sj)]  # 시작 위치 큐에 넣고 시작
    visited[si][sj] = 1  # 방문 처리, 이동칸수
    # 큐가 비어있지 않을 동안 실행
    while q:
        i, j = q.pop(0)
        # 그래프의 i,j값이 3이면 도착
        if graph[i][j] == 3:
            return visited[i][j] - 2  # 시작점, 도착점 빼고
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            # 범위내이고, 이동가능위치(1이아님), 방문안함
            if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] != 1 and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # NxN 크기
    graph = [list(map(int, input())) for _ in range(N)]
    si, sj = -1, -1  # 시작 위치
    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                si, sj = i, j
    print(f"#{tc} {bfs(si, sj)}")