def su(x):
    if x == M:
        print(*result)
    else:
        for i in range(N):
            # 방문하지 않았고,
            if not visited[i]:
                # 1번 이상의 인덱스를 채우는 중 -> 이전 자리 존재
                # 이전 자리의 값보다 큰 값만 올 수 있음
                # 0번 인덱스인 경우 그냥 진행
                if x >= 1 and result[x - 1] < nums[i] or x == 0:
                    visited[i] = 1
                    result[x] = nums[i]
                    su(x + 1)
                    visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N
result = [0] * M
su(0)
