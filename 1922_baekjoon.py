def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        rep[y] = x
    else:
        rep[x] = y


N = int(input())    # 컴퓨터 수
M = int(input())    # 선의 수
rep = [i for i in range(N+1)]
edge = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edge.append([w, u, v])
edge.sort()

total = 0   # 비용 계산
cnt = 0     # 연결된 간선의 개수 세기

for w, u, v in edge:
    if find_set(u) != find_set(v):
        union(u, v)
        total += w
        cnt += 1
        if cnt == N-1:
            break
print(total)