def put(k):
    global cnt
    if k == N:
        cnt += 1
    else:
        for j in range(N):
            queen[k] = j    # j: 열 값
            # k번째 채워진 값이 이전과 비교해서 가능한 경우인지 확인
            for i in range(k):
                # k번째 열 값과 i번째 열 값이 다르고 대각선이 아닌경우
                if queen[k] == queen[i] or abs(queen[k] - queen[i]) == k - i:
                    break
            else:
                put(k+1)    # 다음으로 진행


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # NxN
    # 인덱스 - 행, 값 - 열
    queen = [0] * N
    cnt = 0     # 놓는 경우의 수 세기
    put(0)
    print(f"#{tc} {cnt}")