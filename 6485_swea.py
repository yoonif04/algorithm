# 6485번. 삼성시의 버스 노선
import sys

sys.stdin = open("s_input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 버스 노선 수
    counts = [0] * 5001
    for _ in range(N):
        ai, bi = map(int, input().split())  # ai 이상 bi이하 정류장을 다님
        for i in range(ai, bi + 1):
            counts[i] += 1

    P = int(input())
    cj = [int(input()) for _ in range(P)]
    print(f"#{tc}", end=" ")
    for busstop in cj:
        print(counts[busstop], end=" ")
    print()