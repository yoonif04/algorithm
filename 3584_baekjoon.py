T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노드의 수
    # 자식인덱스번호에 부모의 정보를 담을 변수
    par = [0] * (N+1)
    # 자식, 부모 정보를 담기
    for _ in range(N-1):
        p, c = map(int, input().split())
        par[c] = p
    f1, f2 = map(int, input().split())

    # f1의 조상을 방문처리하기
    visited = [0] * (N+1)
    while f1 > 0:
        visited[f1] = 1
        f1 = par[f1]

    result = 0
    # f2의 조상을 방문하며 공통조상인지 확인하기
    while f2 > 0:
        if visited[f2] == 1:
            result = f2
            break
        f2 = par[f2]

    print(result)
