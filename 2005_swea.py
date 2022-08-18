T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 파스칼 삼각형을 담을 변수 2*N+1개를 0으로 채워서
    pascal = [[0]*(2*N+1) for _ in range(N)]
    pascal[0][(2*N+1)//2] = 1   # 0행의 중심에 1 채우기
    # 순회하면서 삼각형 만들기
    for i in range(1, N):           # 1~N-1행
        for j in range(1, 2*N):     # 1~2N-1열까지(어차피 끝열0)
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j+1]  # 좌상단+우상단

    print(f"#{tc}")
    for i in range(N):
        for j in range(2*N):
            if pascal[i][j]:    # 0이 아니면
                print(pascal[i][j], end=" ")
        print()