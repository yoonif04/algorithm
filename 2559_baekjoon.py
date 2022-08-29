# N:온도 측정한 전체 날짜, K:합 구하기 위한 연속적인 날짜 수
N, K = map(int, input().split())
temp = list(map(int, input().split()))  # 온도

# 처음 K개 온도 합
sum_temp = sum(temp[0:K])
max_sum = sum_temp

# K번 인덱스부터 끝까지 해당 인덱스의 값은 더하고
# 해당 인덱스에서 K앞의 인덱스의 값은 빼주기
for i in range(K, N):
    sum_temp += temp[i] - temp[i-K]
    if max_sum < sum_temp:
        max_sum = sum_temp

print(max_sum)