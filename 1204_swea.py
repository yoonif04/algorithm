# 1204 문제
# import sys
# sys.stdin = open("input.txt", "r")
# 테스트 케이스의 수
T = int(input())

for test_case in range(1, T+1):
    test_case_num = int(input())
    # 점수 정보 담긴 리스트
    scores = list(map(int, input().split()))
    # 점수의 빈도를 기록할 리스트 0~100점
    counts = [0]*(101)
    # 점수 순회하면서 빈도 증가
    for score in scores:
        counts[score] += 1

    # 빈도가 높은 점수 기록할 변수
    maxidx = -1
    for idx in range(len(counts)):
        if counts[maxidx] <= counts[idx]:
            maxidx= idx
    print(f"#{test_case_num} {maxidx}")