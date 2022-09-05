n = int(input())
nums = list(map(int, input().split()))
result = [0] * n
# 각 자리까지 만들 수 있는 최대값
result[0] = nums[0]
# 1번 인덱스부터 끝까지
for i in range(1, n):
    # i번까지의 최대값 -> i번의 숫자 혹은 i번의 숫자와 그 전까지의 최대값 합
    result[i] = max(nums[i], nums[i] + result[i-1])

print(max(result))