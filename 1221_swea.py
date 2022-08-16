T = int(input())
for test_case in range(1, T+1):
    tc, N = input().split()
    nums = list(input().split())
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    counts = [0] * 10   # 개수 셀 변수
    # nums에서 하나씩 꺼내와서 num_list에 대응되는 인덱스 찾아 증가
    for num in nums:
        for i in range(10):
            if num_list[i] == num:
                counts[i] += 1

    print(tc)
    for i in range(10):
        for j in range(counts[i]):   # 개수만큼
            print(num_list[i], end=" ")   # num_list에 대응되는 값 출력
    print()