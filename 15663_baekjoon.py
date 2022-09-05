def su(x):
    if x == M:
        if value not in result:
            result.append(value[:]) # 얕은 복사 하지 않도록
    else:
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                value[x] = nums[i]
                su(x+1)
                visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N  # N개의 숫자 방문여부
value = [0] * M     # M개 자리 숫자
result = []        # 결과 담을 리스트
su(0)

for x in result:
    print(*x)