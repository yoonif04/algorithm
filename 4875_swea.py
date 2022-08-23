# 4875. 미로
import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # NxN 미로 크기
    graph = [list(map(int,input())) for _ in range(N)]
    # 시작 점 찾기
    x = N-1
    for i in range(N-1):
        if graph[x][i] == 2:
            y = i

    # 방향 - 상,하,좌,우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방향을 담을 스택 - 처음 방향 담고 시작
    stack = [(x, y)]

    # 정답을 나타낼 변수
    answer = 0
    while stack:    # 스택이 비어있지 않는 동안
        # 스택에서 좌표 꺼내기
        x, y = stack.pop()
        for d in range(4):  # 방향 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 내이고
            if 0<= nx < N and 0<= ny < N:
                # 3값이라면 정답을 찾음 -> answer를 바꾸고 탈출
                if graph[nx][ny] == 3:
                    answer = 1
                    break
                # 0값이라면 이동 가능 -> 스택에 쌓기, 이동했음을 표시(임의로 5)
                if not graph[nx][ny]:
                    stack.append((nx, ny))
                    graph[nx][ny] = 5
        # 정답 찾았으면 탈출
        if answer:
            break

    print(f"#{tc} {answer}")