import copy
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def move():
    global virus
    # 미생물 수만큼 반복
    stack = []
    while virus:
        x, y, num, dir = virus.pop(0)
        if x == -1 and y == -1:
            continue
        nx, ny = x + dx[dir], y + dy[dir]
        if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
            if dir == UP:
                dir = DOWN
            elif dir == DOWN:
                dir = UP
            elif dir == LEFT:
                dir = RIGHT
            elif dir == RIGHT:
                dir = LEFT
            num //= 2
        stack.append([nx, ny, num, dir])

    # 내림차순 정렬 - 같은 위치라면 미생물 수가 많은 것이 앞에 온다.
    stack.sort(reverse=True)

    # 중복된 길이만큼
    for i in range(len(stack)):
        for j in range(i+1, len(stack)):
            v1 = stack[i]
            v2 = stack[j]
            # 같은 위치라면 앞의 미생물이 더 많다
            if v1[0] == v2[0] and v1[1] == v2[1]:
                v1[2] += v2[2]
                v2[2] -= v2[2]
                v2[0] = v2[1] = -1
    virus = copy.deepcopy(stack)


T = int(input())
for tc in range(1, T+1):
    # NxN, M:격리 시간, K:미생물 군집
    N, M, K = map(int, input().split())

    virus = []
    for _ in range(K):
        x, y, num, dir = map(int, input().split())
        virus.append([x, y, num, dir-1])

    for _ in range(M):
        move()

    sumV = 0
    for v in virus:
        sumV += v[2]

    print(f"#{tc} {sumV}")