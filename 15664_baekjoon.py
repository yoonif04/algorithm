def su(x):
    if x == M:
        # 방법 1: set 사용
        # set에 들어있는 값들 -> 해쉬 가능해야 함
        # 문자열, 숫자, 튜플 가능, 리스트 불가능
        # result_set.add(tuple(result))

        # 방법 2: list 사용
        # 리스트 사용시 그냥 result값을 넣으면 얕은 복사
        # 이후 전부 마지막 result 값으로 다 바뀌어 있음
        if result not in result_li:
            result_li.append(result[:])
    else:
        for i in range(N):
            # 아직 숫자 등장 안했고, 1번 인덱스 이상이면 이전 숫자 값 비교
            if not visited[i] and x >= 1 and result[x - 1] <= nums[i] or x == 0:
                visited[i] = 1
                result[x] = nums[i]
                su(x + 1)
                visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N
result = [0] * M
# result_set = set()  # 중복 제거 위한 변수
result_li = []
su(0)
# set에서 하나씩 꺼내서 출력
for x in result_li:
    print(*x)
