from collections import deque


def bfs(s):
    q = deque()
    q.append(s)  # 시작 위치, 초 입력
    visited = set()  # 등장한 위치 정보 기록
    visited.add(s)
    dist = [-1] * MAX
    dist[s] = 0     # 시작 점

    while q:
        x = q.popleft()

        if x * 2 not in visited and x * 2 < MAX:
            visited.add(x * 2)
            q.append(x * 2)
            dist[x*2] = dist[x]
        if x - 1 not in visited and x - 1 >= 0:
            visited.add(x - 1)
            q.append(x - 1)
            dist[x-1] = dist[x] + 1
        if x + 1 not in visited and x + 1 < MAX:
            visited.add(x + 1)
            q.append(x + 1)
            dist[x+1] = dist[x] + 1

    return dist[K]


N, K = map(int, input().split())
MAX = 100010
print(bfs(N))
