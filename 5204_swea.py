# 5204. 병합 정렬
def merge(left, right):
    global cnt
    merged_arr = []
    l = r = 0

    # 왼쪽의 마지막 값이 오른쪽의 마지막 값보다 크면 갯수 증가
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0

    new = merge_sort(nums)
    print(f"#{tc} {new[len(new) // 2]} {cnt}")