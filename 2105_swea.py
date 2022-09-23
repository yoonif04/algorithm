# 2105. [모의 SW 역량테스트] 디저트 카페
# 대각선 방향 이동 - 반시계방향
di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]


def dessert(si, sj, dir, cnt):
    global num_dessert
    # 직진하거나 꺾거나, 3까지오면 끝
    if dir < 3:
        temp = dir + 2
    else:
        temp = dir + 1
    # print("temp, dir", temp, dir)
    for d in range(dir, temp):
        # 새로운 위치
        ni, nj = si + di[d], sj + dj[d]
        # 시작점으로 다시 도착했다면
        if start[0] == ni and start[1] == nj:
            # 최대값인지 비교 후 갱신
            num_dessert = max(num_dessert, cnt)
            return
        # 범위내이면
        if 0 <= ni < N and 0 <= nj < N and not d_visited[graph[ni][nj]]:
            d_visited[graph[ni][nj]] = 1  # 디저트 종류 체크
            dessert(ni, nj, d, cnt + 1)  # 다음 함수 호출
            d_visited[graph[ni][nj]] = 0  # 디저트 종류 체크 해제
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    d_visited = [0] * 101  # 디저트 종류 중복여부
    num_dessert = -1  # 먹을 수 있는 디저트의 수

    # 시작 지점 고정 후
    for i in range(N - 2):
        for j in range(1, N - 1):
            start = (i, j)  # 시작점
            d_visited[graph[i][j]] = 1  # 디저트 종류 체크
            dessert(i, j, 0, 1)  # 함수 호출
            d_visited[graph[i][j]] = 0  # 디저트 종류 체크 해제

    print(f"#{tc} {num_dessert}")