T = int(input())
for test_case in range(1, T + 1):
    # N*N 배열, M*M: 파리채
    N, M = map(int, input().split())
    # 파리 수
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 순회하면서 최대값 찾기
    max_val = 0
    # 왼쪽 상단 고정점
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_flies = 0  # 죽일 수 있는 파리 수
            # 파리채 순회
            for x in range(i, i + M):
                for y in range(j, j + M):
                    sum_flies += nums[x][y]
                if sum_flies > max_val:
                    max_val = sum_flies
    print(f"#{test_case} {max_val}")