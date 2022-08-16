T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 당근 개수
    carrots = list(map(int,input().split()))  # 당근 크기 정보

    cnt = 1
    max_val = 1
    for i in range(1, N):
        if carrots[i-1] < carrots[i]:
            cnt += 1
            if max_val < cnt:
                max_val = cnt
        else:
            cnt = 1
    print(f"#{tc} {max_val}")