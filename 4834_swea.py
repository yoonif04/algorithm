# List1: 숫자카드
# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int,input()))  # 숫자들
    counts = [0]*10  # 장수를 셀 변수
    for num in nums:
        counts[num] += 1
    # card:카드숫자, cnt:장수
    card = cnt = 0
    # 0~9까지 순회하면서
    for idx in range(10):
        if cnt <= counts[idx]:   # 장수가 많거나 같으면(큰 수로)
            card = idx   # 카드값 변경
            cnt = counts[idx]           # 장수 변경
    print(f"#{test_case} {card} {cnt}")