def binary_search(target):
    l = 0
    r = N - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1


N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if binary_search(target):
        print(1)
    else:
        print(0)