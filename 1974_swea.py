T = int(input())
for test_case in range(1, T + 1):
    # 스도쿠 숫자
    nums = [list(map(int, input().split())) for _ in range(9)]
    # 검증
    flag = True
    # 순회하면서 검사
    # 행 검사, 열검사
    # 격자 검사

    for i in range(9):
        counts_row = [0] * 10  # 10칸짜리 1~9셀 수 있도록
        counts_col = [0] * 10  # 10칸짜리 1~9셀 수 있도록
        for j in range(9):
            # 행 탐색 - counts_row변수에 1까지만 담길 수 있다
            counts_row[nums[i][j]] += 1
            if counts_row[nums[i][j]] > 1:
                flag = False
                break

            # 열 탐색 - counts_col변수에 1까지만 담길 수 있다
            counts_col[nums[j][i]] += 1
            if counts_col[nums[j][i]] > 1:
                flag = False
                break

        if not flag:
            break

    # 격자 -> 0, 3, 6행, 0,3,6열이 왼쪽 상단
    num_list = [0, 3, 6]
    for i in num_list:
        for j in num_list:
            counts_box = [0] * 10  # 10칸짜리 1~9셀 수 있도록
            # 왼쪽 상단부터 3칸씩
            for x in range(i, i+3):
                for y in range(j, j+3):
                    counts_box[nums[x][y]] += 1
                    if counts_box[nums[x][y]] > 1:
                        flag = False
                        break

    print(f"#{test_case} {int(flag)}")