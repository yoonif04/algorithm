graph = [[0]*101 for _ in range(101)]

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            graph[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if graph[i][j] != 0:
            cnt += 1
print(cnt)