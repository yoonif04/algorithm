N = int(input())
cnt = [0]*(N+1)

for i in range(2, N+1):
    # 전의 값 + 1
    cnt[i] = cnt[i - 1] + 1
    # 2의 배수이면 2로 나눈몫 + 1과 자기자신 중 작은값으로
    if i % 2 == 0:
        cnt[i] = min(cnt[i//2] + 1, cnt[i])
    # 3의 배수이면 3으로 나눈몫 + 1과 자기자신 중 작은 값으로
    if i % 3 == 0:
        cnt[i] = min(cnt[i//3] + 1, cnt[i])

print(cnt[N])
