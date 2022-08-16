T = int(input())
for test_case in range(1, T+1):
    # N:수강생 수, K:과제 제출한 학생 수
    N, K = map(int, input().split())
    # 과제 제출한 학생 번호
    solved = list(map(int, input().split()))
    print(f"#{test_case}", end=' ')
    # 1번~N번 학생 중 solved에 없는 학생 출력
    for i in range(1, N+1):
        if i not in solved:
            print(i, end=' ')
    print()