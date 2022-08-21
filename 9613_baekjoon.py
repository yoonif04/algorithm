def gcd(a,b):
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
    case = list(map(int, input().split()))
    n = case[0]
    nums = case[1:]
    sum_all_cases = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                sum_all_cases += gcd(nums[i], nums[j])
    print(sum_all_cases)

