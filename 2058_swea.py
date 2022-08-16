n = int(input())
sum_n = 0
while n > 0:
    sum_n += n % 10  # 10으로 나눈 나머지
    n //= 10  # 10으로 나눈 몫
print(sum_n)
