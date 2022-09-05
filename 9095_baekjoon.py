T = int(input())
for _ in range(T):
    n = int(input())
    result = [0] * 12   # n은 양수 11보다 작음
    # 4 -> 1의 경우에 3을 더함
    # 2의 경우에 2를 더함
    # 3의 경우에 1을 더함
    result[1] = 1
    result[2] = 2
    result[3] = 4

    for i in range(4, n+1):
        result[i] += result[i-3] + result[i-2] + result[i-1]

    print(result[n])