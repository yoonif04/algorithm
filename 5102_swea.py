# 5102. 노드의 거리
def bfs(S, G):  # S에서 출발
    # 방문여부 및 경로 정보 담을 변수
    visited = [0] * (V + 1)
    q = [S]  # 시작 노드 담고 시작
    visited[S] = 1  # 방문
    # 큐가 비어있지 않은 동안
    while q:
        now = q.pop(0)
        if now == G:
            return visited[now] - 1
        # now의 인접리스트 순회하며 간선정보 확인
        for next in graph[now]:
            # 방문하지 않았다면, 방문처리와 몇개의 간선을 지나는지, 큐에 넣기
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
    return 0


T = int(input())
for tc in range(1, T + 1):
    # V:노드의 개수(1번부터), E: 간선 개수
    V, E = map(int, input().split())
    # 방향 정보 담긴 인접리스트
    graph = [[] for _ in range(V + 1)]
    # graph에 방향 정보 담기
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # S:출발 노드, G: 도착 노드
    S, G = map(int, input().split())
    print(f"#{tc} {bfs(S, G)}")