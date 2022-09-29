# 5249. 최소 신장 트리 - Prim
def prim(r, V):
    # r에서 시작, 마지막 노드 번호V
    MST = [0] * (V + 1)  # MST에 포함되는지
    MST[r] = 1  # 시작 정점 추가

    s = 0  # 가중치 합

    # V개의 정점 찾기
    for _ in range(V):
        u = 0
        minV = 100
        # V+1개 노드 중 MST에 포함되었고
        for i in range(V + 1):
            if MST[i] == 1:
                # MST에 포함된 정점의 인접 정점
                for j in range(V + 1):
                    # 인접하고, 가중치가 가장 작고 MST에 아직 포함 안된 경우
                    if 0 < adjM[i][j] < minV and MST[j] == 0:
                        u = j
                        minV = adjM[i][j]
        # 선택된 인접 정점의 가중치를 더하고 MST에 추가
        s += minV
        MST[u] = 1
    return s


T = int(input())
for tc in range(1, T + 1):
    # V:마지막 노드번호, E:간선의 개수
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w
    print(f"#{tc} {prim(0, V)}")


# 5249. 최소 신장 트리 - Kruskal
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    # V:마지막 노드번호, E:간선의 개수
    V, E = map(int, input().split())
    edge = []
    rep = [i for i in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([w, v, u])

    edge.sort()

    result = 0  # 가중치의 합
    cnt = 0  # 선택한 간선의 수
    # edge에서 정보를 꺼내서
    for w, v, u in edge:
        # 사이클이 아니라면
        if find_set(u) != find_set(v):
            union(u, v)  # 합치기
            cnt += 1  # 선택한 간선의 수 증가
            result += w  # 가중치의 합 증가
            # 만약 노드의 개수 - 1 만큼 선택했다면 -> 선택완료
            if cnt == V:
                break

    print(f"#{tc} {result}")
