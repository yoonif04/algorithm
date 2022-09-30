# 4012. [모의 SW 역량테스트] 요리사
def comb(i):
    global minV
    # 조합 완성되면 리스트에 담기
    if i == R:
        # 완성된 조합 c , c에 없는거 하나 만들기
        # another = []
        # for i in range(1, N + 1):
        #     if i not in c:
        #         another.append(i)
        another = [i for i in range(1, N + 1) if i not in c]

        # 각각 시너지 구하기
        s1 = 0
        s2 = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                s1 += foods[c[i]-1][c[j]-1] + foods[c[j]-1][c[i]-1]
                s2 += foods[another[i]-1][another[j]-1] + foods[another[j]-1][another[i]-1]

        # 합이 최소인지
        diff = abs(s1 - s2)
        # if diff < minV:
        #     minV = diff
        minV = min(diff, minV)
        return

    else:
        for j in range(1, N + 1):
            if i == 0 or (not used[j] and c[i - 1] < j):
                used[j] = 1
                c[i] = j
                comb(i + 1)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]

    # N 까지에서 N//2개 조합 만들기
    R = N // 2
    c = [0] * R
    used = [0] * (N + 1)
    minV = 20000
    comb(0)
    print(f"#{tc} {minV}")

