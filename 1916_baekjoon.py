import heapq


def dijkstra(s, V):
    pq = []
    heapq.heappush(pq, (0, s))
    D[s] = 0

    while pq:
        w, x = heapq.heappop(pq)

        if D[x] < w:
            continue

        for nw, nx in adjL[x]:
            dist = w + nw

            if D[nx] > dist:
                heapq.heappush(pq, (dist, nx))
                D[nx] = dist


INF = 100000*1001
N = int(input())  # 도시 개수
M = int(input())  # 버스 개수
# adjM = [[INF] * (N + 1) for _ in range(N + 1)]
adjL = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adjL[u].append((w, v))

# S: 시작, E: 도착
S, E = map(int, input().split())
D = [INF] * (N + 1)  # 거리
dijkstra(S, N)

print(D[E])
