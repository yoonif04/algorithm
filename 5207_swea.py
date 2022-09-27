# 5207. 이진 탐색
def binary_search(arr, l, h, key, dir):
    if l > h:
        return False
    mid = (l + h) // 2
    if key == arr[mid]:
        return True
    elif key < arr[mid]:
        if dir == "n" or dir == 'right':
            dir = 'left'
            return binary_search(arr, l, mid - 1, key, dir)
        else:
            False
    elif key > arr[mid]:
        if dir == 'n' or dir == 'left':
            dir = 'right'
            return binary_search(arr, mid + 1, h, key, dir)
        else:
            False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    targets = list(map(int, input().split()))
    cnt = 0
    for target in targets:
        if binary_search(arr, 0, N - 1, target, "n"):
            cnt += 1
    print(f"#{tc} {cnt}")
