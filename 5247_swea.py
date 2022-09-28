from collections import deque
def bfs(s, e):
    # 시작 숫자 s에서 e 만들기
    q = deque()
    q.append(s)

    cnt = 0  # 연산횟수 세기
    visited = set()  # 숫자 등장여부 체크
    visited.add(s)

    # 큐가 비어있지 않는동안
    while q:
        # 큐의 길이만큼
        for _ in range(len(q)):
            num = q.popleft()

            # e가 만들어졌으면 연산횟수 반환 후 종료
            if num == e:
                return cnt
            # 새로운 숫자 넣기
            for next in (num + 1, num - 1, num * 2, num - 10):
                if next <= INF and next not in visited:
                    visited.add(next)
                    q.append(next)
        cnt += 1


INF = 1000000
T = int(input())
for tc in range(1, T + 1):
    # N -> M 만들기
    N, M = map(int, input().split())
    print(f"#{tc} {bfs(N, M)}")
