# 1795. 인수의 생일 파티
from collections import deque


def dijkstra(s, graph):
    D = [INF] * (N + 1)  # 거리 정보
    D[s] = 0  # 시작점
    q = deque()
    q.append(s)
    # 큐가 비지 않는 동안
    while q:
        node = q.popleft()
        # node와 인접한 경우
        for next, w in graph[node]:
            # 기존 거리보다 돌아가는게 작다면 갱신
            if D[node] + w < D[next]:
                D[next] = D[node] + w
                q.append(next)  # 큐에 다음 정점 넣기
    return D


T = int(input())
for tc in range(1, T + 1):
    # 1~N번집, X:인수의 집
    N, M, X = map(int, input().split())
    INF = 100000
    adj_go = [[] for _ in range(N + 1)]
    adj_come = [[] for _ in range(N + 1)]

    # 도로 연결 정보
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj_go[u].append((v, w))  # 집에 돌아올 때
        adj_come[v].append((u, w))  # 파티 갈 때

    go_dist = dijkstra(X, adj_go)
    come_dist = dijkstra(X, adj_come)
    maxV = 0
    for i in range(1, N + 1):
        dist = go_dist[i] + come_dist[i]
        if dist > maxV:
            maxV = dist
    print(f"#{tc} {maxV}")