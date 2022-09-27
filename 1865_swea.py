def work(i, s):
    global maxV
    # i: 몇번째인지 => N이면 완료
    if i == N:
        # 최대값보다 큰지 비교 후 갱신
        if s > maxV:
            maxV = s
        return
    # 합이 maxV보다 작으면 가능성x -> 곱하는 값들이 1보다 작기때문
    elif s <= maxV:
        return
    else:
        for j in range(N):
            # 방문하지 않았다면
            if visited[j] == 0:
                visited[j] = 1
                work(i+1, s*percent[i][j]/100)
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    # 선택 여부 체크
    visited = [0] * N
    maxV = 0    # 최대값 기록할 변수
    work(0, 1)
    maxV *= 100
    print(f"#{tc} {maxV:.6f}")
