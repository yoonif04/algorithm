def gcd(a,b):
    if a < b:
        a, b = b, a
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# 두 수 입력받기
a, b = map(int, input().split())
# 최대공약수 숫자만큼 1이 출력됨
for i in range(gcd(a,b)):
    print(1, end="")