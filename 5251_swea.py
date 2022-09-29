# 5251. 최소 이동 거리
def dijkstra(s, V):
    # s에서 시작, V가 마지막 번호
    U = [0] * (V+1)     # 비용 결정된 정점
    U[s] = 1    # 시작점
    # 시작점부터의 가중치
    for i in range(V+1):
        D[i] = adjM[s][i]

    for _ in range(V+1):
        u = 0
        minV = INF
        # V+1개 정점에서 아직 비용 결정안되었고, 작으면
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                u = i
                minV = D[i]
        U[u] = 1
        # 고른 u에 인접한 정점들의 거리정보 갱신
        for v in range(V+1):
            if 0 < adjM[u][v] < INF:
                D[v] = min(D[v], D[u] + adjM[u][v])


T = int(input())
for tc in range(1, T+1):
    # N:마지막 연결지점 번호, E: 도로의 개수
    N, E = map(int, input().split())
    INF = 100
    adjM = [[INF]*(N+1) for _ in range(N+1)]
    # 자기 자신 0으로 만들기
    for i in range(N+1):
        adjM[i][i] = 0
    # 도로 연결 정보, 가중치 입력
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    # 거리정보
    D = [0] * (N+1)
    dijkstra(0, N)
    print(f"#{tc} {D[N]}")