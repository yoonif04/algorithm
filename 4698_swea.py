def get_prime(start, end):
    arr = [True] * (end+1)
    m = int((end+1)**0.5)
    for i in range(2, m+1):
        if arr[i]:
            for j in range(i+i, end+1, i):
                arr[j] = False
    return [i for i in range(2, end+1) if arr[i]==True and i>=start]

T = int(input())
for test_case in range(1, T+1):
    D, A, B = map(int, input().split())
    cnt = 0  # 특별한 소수를 셀 변수
    sosu_list = get_prime(A, B)

    for sosu in sosu_list:
        if str(D) in str(sosu):
            cnt += 1
    print(f"#{test_case} {cnt}")

# 4698. 테네스의 특별한 소수 - 교수님 풀이
n = 10**6
arr = [True] * (n+1)
arr[1] = False   # 1->소수아님
m = int(n**0.5)
for i in range(2, m+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

T = int(input())
for test_case in range(1, T+1):
    D, A, B = map(int, input().split())
    cnt = 0  # 특별한 소수를 셀 변수
    # 범위는 A부터 B까지
    for i in range(A, B+1):
        if arr[i] == True:
            if str(D) in str(i):
                cnt += 1
    print(f"#{test_case} {cnt}")