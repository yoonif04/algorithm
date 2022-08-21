def get_prime(n, k):
    # n까지의 수 중 소수 찾기
    # k번째 지우는 수
    arr = [True] * (n+1)
    cnt = 0     # 몇 번 지웠는지
    # 2~n까지 중
    for i in range(2, n+1):
        if arr[i]:  # 소수라면
            cnt += 1    # 횟수 증가
            if cnt == k:
                return i

            for j in range(i+i, n+1, i):
                if arr[j]:
                    arr[j] = 0
                    cnt += 1
                    if cnt == k:
                        return j

a, b = map(int, input().split())
print(get_prime(a, b))