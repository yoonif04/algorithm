N = int(input())
size = 10001
nums = [0] * size

for i in range(N):
    num = int(input())
    nums[num] += 1

for i in range(1, size):
    if not nums[i]:
        for j in range(nums[i]):
            print(i)