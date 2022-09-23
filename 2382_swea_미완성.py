# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def move():
    # 미생물 수만큼 반복
    for i in range(K):
        x, y, num, dir = virus[i]
        if x != -1 and y != -1:
            nx, ny = x + dx[dir-1], y + dy[dir-1]
            # 경계선에 닿으면
            if nx == 0 or nx == N-1:
                if dir == UP:
                    dir = 1
                else:
                    dir = 0
                num //= 2
            if ny == 0 or ny == N-1:
                if dir == LEFT:
                    dir = 3
                else:
                    dir = 2
                num //= 2
            virus[i] = [x, y, num, dir]

    # 같은 위치에 있는지 확인
    for i in range(K):
        for j in range(i+1, K):
            v1 = virus[i]
            v2 = virus[j]
            # 같은 위치라면
            if v1[0] == v2[0] and v1[1] == v2[1]:
                # 미생물 수 비교 후 방향 바꾸고 합치기
                if v1[2] < v2[2]:
                    v2[2] += v1[2]
                    v1[2] -= v1[2]
                    v1[0] = v1[1] = -1  # 위치 -1로
                else:
                    v1[2] += v2[2]
                    v2[2] -= v1[2]
                    v2[0] = v2[1] = -1


T = int(input())
for tc in range(1, T+1):
    # NxN, M:격리 시간, K:미생물 군집
    N, M, K = map(int, input().split())

    virus = []
    for _ in range(K):
        x, y, num, dir = map(int, input().split())
        virus.append([x, y, num, dir])

    for _ in range(M):
        move()

    sumV = 0
    for i in range(K):
        sumV += virus[i][2]

    print(f"#{tc} {sumV}")