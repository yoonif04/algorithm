def su(x):
    if x == M:
        print(*result)
    else:
        # N개의 숫자 인덱스 만큼
        for i in range(N):
            # 방문하지 않았다면
            if not visited[i]:
                visited[i] = 1      # 방문처리
                result[x] = nums[i] # x번째 자리를 i번째 수로 채우기
                su(x+1)     # 다음으로
                visited[i] = 0  # 방문 안한거로 다시
    return


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N
result = [0] * M
su(0)