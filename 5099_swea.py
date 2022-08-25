# 5099. 피자 굽기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    fire = []
    p = 1  # 피자번호
    # 화덕에 피자 채우기
    for _ in range(N):
        fire.append((p, pizza[p - 1]))
        p += 1

    # 피자 굽기 - 화덕에 한개 남을때까지
    while len(fire) != 1:
        # 피자 꺼내기, v:꺼낸피자번호, cheese:치즈양
        v, cheese = fire.pop(0)
        # 치즈 양을 반으로 나눴을 때 0이면
        if cheese // 2 == 0:
            # 들어갈 피자가 남았으면 넣어주기
            if p <= M:
                fire.append((p, pizza[p - 1]))
                p += 1
        # 치즈 양을 반으로해서 다시 넣어주기
        else:
            fire.append((v, cheese // 2))
    print(f"#{tc} {fire[0][0]}")