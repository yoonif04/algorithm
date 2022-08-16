T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 좌표 하나씩 순회
    # 각 좌표에서 +, x 모양대로 이동 - 각 모양에 맞는 변수에 값 합하기
    # 상, 하, 좌, 우, 좌상단, 우상단, 좌하단, 우하단
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]

    max_sum = 0   # 퇴치한 파리수 합의 최대값을 담을 변수
    # 행, 열 순회
    for i in range(N):
        for j in range(N):
            sum_plus = nums[i][j]    # +모양인 경우 퇴치한 파리수 합
            sum_cross = nums[i][j]   # x모양인 경우 퇴치한 파리수 합
            for d in range(8):   # 8방향으로 이동
                for m in range(1, M):   # 세기만큼
                    ni = i + m * di[d]
                    nj = j + m * dj[d]
                    if 0 <= ni < N and 0 <= nj < N:   # 범위 내이고
                        if 0 <= d < 4:    # 0~3까지는 +모양
                            sum_plus += nums[ni][nj]
                        else:  # 4이상은 x모양
                            sum_cross += nums[ni][nj]
            # 최대값 갱신
            if max_sum < sum_plus:
                max_sum = sum_plus
            if max_sum < sum_cross:
                max_sum = sum_cross
    print(f"#{test_case} {max_sum}")