def su(x):
    if x == M:
        print(*result)
    else:
        # N개의 숫자 개수만큼 반복
        for i in range(N):
            # 1번째자리 채우고 있다면 -> 이전 값 채워져있음
            # 이전값보다 크거나 같은 값만 가능
            # 첫번째 자리 채우고 있다면 그냥 진행
            if x >= 1 and result[x-1] <= nums[i] or x == 0:
                result[x] = nums[i]
                su(x+1)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = [0] * M
su(0)