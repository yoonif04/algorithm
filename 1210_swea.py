for _ in range(10):
    tc = int(input())  # 테스트 케이스 번호
    N = 100  # N행 N열
    # 사다리정보 N행N열 1:이동가능, 0:이동불가
    ladders = [list(map(int, input().split())) for _ in range(N)]
    # 아래에서부터 거꾸로 올라가기
    # 초기 위치 -> 2인 값 위치 - 마지막행
    x = N - 1
    # 초기 위치 - 열 탐색
    for j in range(N):
        if ladders[N - 1][j] == 2:
            y = j

    # 좌, 우, 상
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    # x가 0이면 종료됨 - 사다리 제일 윗부분
    while x > 0:
        # 좌, 우, 상 순서대로 이동가능한지 확인
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 위치가 배열 내이고, 사다리 1(이동가능)
            if 0 <= nx < N and 0 <= ny < N and ladders[nx][ny] == 1:
                x, y = nx, ny  # 위치 이동
                ladders[nx][ny] = 0  # 지나간 곳 다시 못가도록
                break
    print(f"#{tc} {y}")