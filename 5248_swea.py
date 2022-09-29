# 5248. 그룹 나누기
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    # 1~N번, M장의 신청서
    N, M = map(int, input().split())
    # 그룹 정보
    group = list(map(int, input().split()))
    # 대표
    rep = [i for i in range(N+1)]

    # 신청서가 빌때까지 꺼내서 합치기
    while group:
        x = group.pop(0)
        y = group.pop(0)
        union(x, y)

    result = set()  # 그룹 개수 셀 변수
    # 1번~N번까지 대표를 찾아서 셋에 넣기
    for i in range(1, N+1):
        result.add(find_set(i))
    print(f"#{tc} {len(result)}")

