# 5205. 퀵 정렬
def partition(l, r):
    pivot = nums[l]
    i, j = l, r

    while i <= j:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[j] = nums[j], nums[l]
    return j


def quicksort(l, r):
    if l < r:
        s = partition(l, r)
        quicksort(l, s - 1)
        quicksort(s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    N = len(nums)
    quicksort(0, N - 1)
    print(f"#{tc} {nums[N // 2]}")