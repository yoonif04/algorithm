n = int(input())
cnt = [0] * (n+1)
cnt[1] = 1
if n >= 2:
    cnt[2] = 3

for i in range(3, n+1):
    cnt[i] = cnt[i-1] + cnt[i-2]*2

print(cnt[n]%10007)