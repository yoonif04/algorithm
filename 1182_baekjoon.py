# 부분수열의 합
# N개의 정수, 부분수열의 합이 S가 되는지
N, S = map(int, input().split())

subset = list(map(int, input().split()))
cnt = 0     # 개수 셀 변수
# 공집합 제외 부분집합 개수만큼
for i in range(1, 1<<N):
    subset_sum = 0  # 부분집합의 합
    #
    for j in range(N):
        if i & (1<<j):
            subset_sum += subset[j]
    # 부분집합의 합이 S와 같으면 개수 증가
    if subset_sum == S:
        cnt += 1
print(cnt)