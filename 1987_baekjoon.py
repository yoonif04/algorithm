# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, cnt):
    global maxV
    # 이미 등장한 알파벳 -> cnt 확인 후 갱신
    if visited[ord(graph[x][y]) - ord("A")] != 0:
        if cnt > maxV:
            maxV = cnt
    else:
        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # 범위 내이면 함수 호출
            if 0 <= nx < R and 0 <= ny < C:
                visited[ord(graph[x][y]) - ord("A")] = 1
                bfs(nx, ny, cnt + 1)
                visited[ord(graph[x][y]) - ord("A")] = 0   # 다시 되돌리기


# RxC
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
# ord("알파벳") - ord("A") -> 인덱스로 사용
visited = [0] * 30
maxV = 0
bfs(0, 0, 0)
print(maxV)
