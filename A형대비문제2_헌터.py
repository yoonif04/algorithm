import sys
sys.stdin = open("sample_input(1).txt", "r")
from collections import deque
from itertools import permutations
list(permutations([-1, -2, -3], 3))

# 순열 - 몬스터로 시작
# 몬스터 M개 손님 M명
# 1~M번손님 * (나머지를 순열로 바꾼 것)
# 최단거리 합
# [1, 2, 3]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(s, e):
    # 시작값, 끝값
    visited = [[0]*N for _ in range(N)]
    q = deque()
    # s가 0이면 0,0부터 시작
    if s == 0:
        q.append((0, 0))
        visited[0][0] = 1
    # 아니라면 시작값에 해당하는 인덱스 찾기
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == s:
                    q.append((i, j))
                    visited[i][j] = 1
                    break
    # 반복
    while q:
        i, j = q.popleft()
        if graph[i][j] == e:
            return visited[i][j] - 1
        else:
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 가로세로길이
    graph = [list(map(int, input().split())) for _ in range(N)]
    customers = []  # 손님 번호 담을 리스트
    monsters = []   # 몬스터 번호 담을 리스트
    # 손님과 몬스터 찾아서 리스트로 만들기
    for i in range(N):
        for j in range(N):
            # 0이 아니면 손님 혹은 몬스터
            if graph[i][j] > 0:
                monsters.append(graph[i][j])
            if graph[i][j] < 0:
                customers.append(graph[i][j])

    # 손님과 몬스터 순열 만들기
    length = len(customers) + len(monsters)
    perms = list(permutations(customers + monsters, length))

    # 가능한 순열 찾기
    correct_perms = []
    for perm in perms:
        flag = True
        # 첫번째가 몬스터(양수) 마지막이 고객(음수)여야함
        if perm[0] > 0 and perm[-1] < 0:
            # 1번인덱스부터 마지막 인덱스까지
            # 만약 고객이라면, 이전에 해당 번호의 몬스터 등장했어야 함
            for i in range(1, length):
                if perm[i] < 0:
                    if -perm[i] not in perm[:i]:
                        flag = False
                        break
            if flag:
                correct_perms.append(perm)

    # 최소값 저장할 변수
    min_time = N*N*N*N

    # 순열 하나씩 꺼내서
    for perm in correct_perms:
        time = bfs(0, perm[0])
        for i in range(1, len(perm)):
            time += bfs(perm[i-1], perm[i])
            # time값이 최소값보다 커지면 탐색 중지
            if time > min_time:
                break
        # 최소값인지 비교 후 갱신
        if min_time > time:
            min_time = time
    print(f"#{tc} {min_time}")
