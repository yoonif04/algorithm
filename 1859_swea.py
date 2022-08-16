import sys
sys.stdin = open("input.txt", "r")
def find_max_price_idx(prices, s, e):
    # s부터 e까지 중에서 max값인 가격과 인덱스 반환
    max_price, max_idx = 0, -1
    for i in range(s, e):
        if max_price < prices[i]:
            max_price = prices[i]
            max_idx = i
    return max_price, max_idx

def find_buy_cnt(prices, s, max_idx):
    # s부터 e까지 중에서 max보다 작은 값을 찾아
    # 산 가격과 개수 반환
    buy, buy_cnt = 0, 0
    for i in range(s, max_idx):
        if prices[i] < prices[max_idx]:
            buy += prices[i]
            buy_cnt += 1
    return buy, buy_cnt

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    profit, s = 0, 0
    while s < N:
        max_price, max_idx = find_max_price_idx(prices, s, N)
        buy, buy_cnt = find_buy_cnt(prices, s, max_idx)
        s = max_idx + 1
        profit += max_price * buy_cnt - buy
    print(f"#{test_case} {profit}")

# 위의 것 - 메모리 살짝 초과됨


# 뒤부터 탐색하는 방법
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    profit = 0
    max_val = nums[N - 1]
    # 뒤에서부터 순회
    for i in range(N - 1, -1, -1):
        # max_val보다 크면 갱신
        if nums[i] > max_val:
            max_val = nums[i]
        # 아니면, 이익만큼 추가
        else:
            profit += max_val - nums[i]

    print(f'#{test_case} {profit}')

