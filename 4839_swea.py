def BinarySearch(page, target):
    start = 1
    end = page
    cnt = 0  # 탐색횟수
    while start <= end:
        middle = (start + end) // 2
        if middle == target:
            cnt += 1
            return cnt
        elif middle > target:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return page + 1


T = int(input())
for test_case in range(1, T + 1):
    # P:전체쪽수 A:A가 찾을번호 B:B가 찾을 번호
    P, PA, PB = map(int, input().split())
    # 탐색 횟수
    cnt_a = BinarySearch(P, PA)
    cnt_b = BinarySearch(P, PB)
    # 횟수 비교 후 승자 출력
    print(f"#{test_case}", end=" ")
    if cnt_a < cnt_b:
        print("A")
    elif cnt_a > cnt_b:
        print("B")
    else:
        print(0)