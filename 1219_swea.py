import sys
sys.stdin = open("input.txt", "r")
def dfs(s):
    visited[s] = 1
    for i in range(node):
        if graph[s][i] and not visited[i]:
            dfs(i)


T = 10
for _ in range(1, T + 1):
    tc, num = map(int, input().split())
    road = list(map(int, input().split()))
    node = 100
    visited = [0]*node

    graph = [[0]*node for _ in range(node)]
    for i in range(0, len(road), 2):
        start = road[i]
        end = road[i+1]
        graph[start][end] = 1

    dfs(0)
    print(f"#{tc} {visited[99]}")