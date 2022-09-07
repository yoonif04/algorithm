from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    stack = [(i, j)]  # 방문가능한 국가 담을 스택
    population = people[i][j]  # 인구 수 담을 변수
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            # 범위 내이고 방문하지 않았다면
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                # 인구 수의 차이가 L이상 R이하 라면
                if L <= abs(people[i][j] - people[ni][nj]) <= R:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    stack.append((ni, nj))
                    population += people[ni][nj]

    # stack 길이 1이라면 방문할 국가 없음
    if len(stack) == 1:
        return False
    # 스택에 담겨있는 연합국가들의 인구 수 조정
    for s in stack:
        i, j = s
        people[i][j] = population//len(stack)
    return True


# NxN크기, 인구 차이 L명이상 R명이하이면 이동 가능
N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

day = 0
# 인구 이동 없을 때까지 반복
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False    # 인구 이동 존재 유무 나타냄
    # 순회하면서
    for i in range(N):
        for j in range(N):
            # 방문하지 않았으면 bfs
            if not visited[i][j]:
                # True 반환되었다면 인구 이동 있었다는 것
                if bfs(i, j):
                    flag = True
    # flag가 False -> 인구 이동 없었음 -> break
    if not flag:
        break
    # day 증가
    day += 1

print(day)
