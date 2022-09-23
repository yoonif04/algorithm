# 1486. 장훈이의 높은 선반
def top(idx, h):
    global minV
    # B와 크거나 같고 최소값보다 작은 경우에만 갱신
    if B <= h < minV:
        minV = h
    # N개 완료 - 종료
    if idx == N:
        return
    top(idx + 1, h)  # 키 포함x
    top(idx + 1, h + height[idx])  # 키 포함


T = int(input())
for tc in range(1, T + 1):
    # 점원수 N, 높이 B
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    minV = 200000  # 20 * 10000
    top(0, 0)
    print('#{} {}'.format(tc, minV - B))