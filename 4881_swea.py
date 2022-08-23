# 4881. 배열 최소 합
def MinSum(x, sub):     # x번째 행, 지금까지의 합
    global result
    # x가 N이랑 같아지면 모든 행 방문 완료
    if x == N:
        if sub < result:
            result = sub

    # sub가 result보다 커지면 그만 둠
    if sub > result:
        return

    # 열 순회하면서 방문가능한지 확인
    for y in range(N):
        # 방문 안했으면 방문 처리, 값 더해서 다음 함수 실행
        if not visited[y]:
            visited[y] = 1
            sub += arr[x][y]
            MinSum(x+1, sub)
            # 다시 방문X, 값 줄여줌
            visited[y] = 0
            sub -= arr[x][y]


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # NxN배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N   # 열 방문 여부 체크
    result = 101    # 최대 10줄, 10보다 작은 자연수
    MinSum(0, 0)
    print(f"#{tc} {result}")
