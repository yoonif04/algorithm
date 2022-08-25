n = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(n):
    r, c = map(int, input().split())
    # 가로, 세로 10칸씩
    for i in range(r, r+10):
        for j in range(c, c+10):
            paper[i][j] = 1

cnt = 0     # 검은색 영역 셀 변수
for i in range(100):
    for j in range(100):
        if paper[i][j] != 0:
            cnt += 1
print(cnt)