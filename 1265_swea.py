T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    # N개 - 나머지 = 나누어 떨어지는 개수
    # 몫**(P개 - 나머지개수) * (몫+1)**(나머지개수)
    divide = N // P
    mod = N % P
    result = (divide ** (P - mod)) * ((divide+1) ** mod)
    print(f'#{tc} {result}')
