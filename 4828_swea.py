# List1 : minmax
# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split())) # 숫자들
    maxVal = minVal = nums[0]
    for i in range(1, N):    # 순회하며 min,max 값 찾기
        if nums[i] > maxVal:
            maxVal = nums[i]
        if nums[i] < minVal:
            minVal = nums[i]
    print(f"#{test_case} {maxVal-minVal}")