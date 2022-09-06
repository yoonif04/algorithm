R, C, W = map(int, input().split())
pascal = [[0]*(2*(R+W) + 1) for _ in range(R+W)]
pascal[0][(2*(R+W))//2] = 1
for i in range(1, R+W):
    for j in range(1, 2*(R+W)):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j+1]

cnt = 0
si = R-1
# 행에서 1이 시작하는 지점은 중심에서 행의 수만큼 왼쪽으로 온 것과 같다.
# 중심: 2*(R+W)//2
# 행의 수: R-1
# C번째 숫자 2*(C-1)
sj = 2*(R+W)//2 - (R-1) + 2*(C-1)

# 시작 행부터 W만큼 반복
result = 0
# 1부터 W까지 반복
for i in range(W):
    # 시작 열은 sj에서 i만큼 뺀 것과 같다
    for j in range(sj-i, sj+i+1, 2):
        # 행은 si에서 i를 더한 것과 같다.
        result += pascal[si+i][j]
print(result)