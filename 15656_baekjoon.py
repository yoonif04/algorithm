def su(x):
    if x == M:
        print(*result)
    else:
        # N개의 숫자만큼 반복
        for i in range(N):
            # x번째 인덱스 채우기
            result[x] = nums[i]     # 값 채우기
            su(x+1)         # 다음칸 채우러 가기


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = [0] * M
su(0)