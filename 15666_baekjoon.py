def su(x):
    if x == M:
        print(*result)
    else:
        # nums에 있는 숫자 개수만큼 
        for i in range(len(nums)):
            # 1번 이상의 인덱스를 채우는 것 -> 이전 자리 이미 채움
            # 이전 자리보다 크거나 같은 값인 경우
            # 0번 인덱스를 채우는 중일 때
            if x >= 1 and result[x-1] <= nums[i] or x == 0:
                result[x] = nums[i]
                su(x+1)


N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = [0] * M
su(0)