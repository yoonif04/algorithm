N = int(input())    # 색종이 장 수
paper = [[0]*1001 for _ in range(1001)]

for n in range(1, N+1):
    r1, c1, w, h = map(int, input().split())
    for i in range(r1, r1+w):
        for j in range(c1, c1+h):
            paper[i][j] = n

paper_cnt = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        n = paper[i][j]
        if n != 0:
            paper_cnt[n] += 1

for i in range(1, N+1):
    print(paper_cnt[i])