# 4880. 토너먼트 카드게임
# 1<2, 1>3, 2<3
def win(left, right):
    # 같은 값이면 번호가 작은 쪽으로
    if cards[left] == cards[right]:
        return left

    # 인덱스 두개를 받아서 누가 이기는지 비교 후 이기는 인덱스 반환
    if cards[left] == 1 and cards[right] == 2:
        return right
    elif cards[left] == 1 and cards[right] == 3:
        return left
    elif cards[left] == 2 and cards[right] == 3:
        return right
    elif cards[left] == 2 and cards[right] == 1:
        return left
    elif cards[left] == 3 and cards[right] == 1:
        return right
    elif cards[left] == 3 and cards[right] == 2:
        return left


def divide(start, end):
    if start > end:
        return False
    # 같은 인덱스 들어오면 아무거나 반환
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        l = divide(start, mid)
        r = divide(mid+1, end)
        return win(l, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 인원수
    cards = list(map(int, input().split()))     # 고른 카드
    result_idx = divide(0, N-1)
    print(f"#{tc} {result_idx+1}")