n, k = map(int, input().split())
pascal = [[0]*(2*n+1) for _ in range(n)]
pascal[0][(2*n+1)//2] = 1
for i in range(1, n):
    for j in range(1, 2*n):
        # 좌측 위 우측 위 값 더하기
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j+1]

print(pascal[n-1][2*k-1])