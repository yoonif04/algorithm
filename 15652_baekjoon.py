def su(n):
    # n이 M과 같은 값이면 자리를 다 채웠음
    if n == M:
        print(*nums)
    else:
        for i in range(1, N+1):
            # 채우는 자리 인덱스가 1 이상이면 -> 이전 자리 존재
            # 이전 자리의 값보다 같거나 큰지 배교
            # 첫번째 자리 채우는 경우 그냥 진행
            if n >= 1 and nums[n-1] <= i or n == 0:
                nums[n] = i     # i값으로 채우기
                su(n+1)         # 다음 자리 채우러 가기
                nums[n] = 0     # 값 되돌리기


N, M = map(int, input().split())
nums = [0]*M
su(0)
