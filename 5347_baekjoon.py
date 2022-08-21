def gcd(a, b):
    if a < b:
        a, b = b, a
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))