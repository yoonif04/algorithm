# 5789번. 현주의 상자 바꾸기
T = int(input())
for tc in range(1, T+1):
    # N:상자개수, Q:작업수행횟수
    N, Q = map(int, input().split())
    box = [0] * (N+1)   # 0으로 초기화 된 상자
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i

    print(f"#{tc}", end=" ")
    for i in range(1, N+1):
        print(box[i], end=" ")
    print()
