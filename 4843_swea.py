def SelectionSort(nums, N):
    # nums: 정수 리스트, N:정수 개수
    for i in range(N - 1):
        minIdx = i
        for j in range(i + 1, N):
            if nums[minIdx] > nums[j]:
                minIdx = j
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
    return nums


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 정수의 개수
    nums = list(map(int, input().split()))  # 정수
    # 정렬
    SelectionSort(nums, N)
    # 출력
    print(f"#{test_case}", end=" ")
    # -1 0 -2 1 -3 2 -4 3 -5 4
    for i in range(1, 6):
        print(nums[-i], nums[i - 1], end=" ")
    print()

# 특별한 정렬 - 교수님 풀이
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())  # 정수의 개수
    numbers = list(map(int, input().split()))  # 정수

    index = 0  # 바꿀 원소의 인덱스 (최대값 or 최소값)
    i = 0   # 탐색을 시작할 위치

    for ni in range(10):
        # 정렬 시작
        for j in range(i, n):  # 최대값 또는 최소값 찾기 시작
            if ni % 2 == 0 and numbers[j] > numbers[index]:
                # 최대값의 인덱스
                index = j
            if ni % 2 == 1 and numbers[j] < numbers[index]:
                # 최소값의 인덱스
                index = j
        i += 1  # 다음에 와야할 원소의 위치 증가
        # 현재 위치와 최대값 최소값의 위치에 있는 원소 자리 바꿔주기
        numbers[ni], numbers[index] = numbers[index], numbers[ni]

    print(f"#{test_case}", end=" ")
    for i in range(10):
        print(f"{numbers[i]}", end=" ")
    print()