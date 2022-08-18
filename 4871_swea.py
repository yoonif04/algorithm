def dfs(v):
    visited[v] = True
    # print(v)
    stack = [0] * (v + 1)
    s_idx = -1
    while True:
        for w in range(1, V + 1):
            # w는 1이고 visited[w]는 0
            if graph[v][w] and not visited[w]:
                s_idx += 1
                stack[s_idx] = v
                v = w
                # print(w)
                visited[w] = True
        else:
            if s_idx != -1:
                v = stack[s_idx]
                s_idx -= 1
            else:
                break


def dfs2(v):
    # print(v)
    visited[v] = True
    for w in range(1, V + 1):
        if graph[v][w] and not visited[w]:
            dfs2(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a][b] = 1
    S, G = map(int, input().split())
    dfs2(S)
    # dfs(S)
    print(f"#{tc}", end=" ")
    if visited[G]:
        print("1")
    else:
        print("0")