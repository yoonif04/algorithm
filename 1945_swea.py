# 1945번. 간단한 소인수분해
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = [2, 3, 5, 7, 11]     # 5개의 소인수
    counts = [0] * len(nums)    # 5개의 소인수 카운팅 할 변수
    # 0번 인덱스부터 시작해서 나누기 반복
    i = 0
    while i < len(nums):
        # nums[i]로 나눠보기
        if N % nums[i] == 0:
            counts[i] += 1  # 카운트 증가
            N //= nums[i]   # N을 나눈 몫으로 바꾸기
        else:   # 안 나눠지면
            i += 1  # 다음 인덱스로

    print(f"#{tc}", *counts)