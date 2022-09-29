# 7465. 창용 마을 무리의 개수
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 대표 정보
    rep = [i for i in range(N+1)]
    # 관계정보 입력받아 합치기
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    # 무리의 수 세기
    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))
    print(f"#{tc} {len(result)}")
