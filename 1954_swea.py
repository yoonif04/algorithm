# 1954 달팽이 숫자
T = int(input())  # 테스트케이스
for tc in range(1, T+1):
    N = int(input())   # 배열 크기 N*N
    arr = [[0]*N for _ in range(N)]  # 0으로 N*N배열 초기화

    # 방향 우,하,좌,상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    num = 1  # 배열에 넣어줄 숫자
    x, y = 0, 0   # 초기 위치
    d = 0    # 방향 나타낼 인덱스

    # 반복하면서 배열 채우기
    while num <= N*N: # N*N까지만 실행
        arr[x][y] = num  # 배열에 숫자 넣기
        num += 1   # 숫자 증가

        # 새로운 위치
        nx = x + dx[d]
        ny = y + dy[d]
        # 새로운 위치가 가능한지 탐색
        # 범위 내이고 배열안에 값 적히지 않은 경우
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            x, y = nx, ny  # 좌표 갱신
        else:  # 그게 아니라면
            d = (d+1) % 4    # 방향 바꾸기 (0~3까지만)
            x += dx[d]       # 방향 바꾼 x값
            y += dy[d]       # 방향 바꾼 y값

    # 결과 출력
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()