# 5209. 최소 생산 비용
def move(i, s):
    global minV
    # i번째 인덱스 - N번 -> 생산 완료
    # 생산비용 s
    if i == N:
        # 최소 생산비용이면 갱신
        if s < minV:
            minV = s
    elif s > minV:
        return
    else:
        for j in range(1, N+1):
            # 방문 안했으면, 이전에 방문한 공장이 아니라면
            if i == 0 or (not visited[i] and j not in visited):
                visited[i] = j
                move(i + 1, s + cost[i][j-1])
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 공장별 생산 비용
    cost = [list(map(int, input().split())) for _ in range(N)]
    # 제품 생산 여부 체크, 어느 공장에서 생산하는지 기록
    visited = [0] * N
    minV = 100*N    # 최소 생산 비용
    move(0, 0)
    print(f"#{tc} {minV}")