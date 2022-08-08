import sys
sys.stdin = open("input.txt", "r")
# 테스트 케이스 10번
T = 10

for test_case in range(1, T+1):
    nums = int(input())  # 빌딩 개수
    buildings = list(map(int, input().split()))  # 빌딩들의 높이 정보
    # 빌딩 정보에서 첫 2개와 마지막 2개는 건물X
    # 빌딩 순회하며 양 옆 2개 빌딩의 길이 비교
    cnt_view = 0 # 조망권 확보된 개수 셀 변수
    # 2번인덱스부터 길이-3번 인덱스까지
    for i in range(2, nums-2):
        now = buildings[i] # 현재 빌딩
        # 주위 빌딩(왼쪽 2곳, 오른쪽 2곳) 담은 리스트
        arounds = [buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2]]
        # 양 옆 2곳과 높이 비교, 현재 빌딩 높이가 더 높다면
        if now > arounds[0] and now > arounds[1] and now > arounds[2] and now > arounds[3]:
            # i += 3  # 높은 빌딩 존재하면 우측 2개의 빌딩은 비교 필요 없음
            # 해당 빌딩의 높이에서 양옆2개씩의 빌딩 중 가장 높은 높이 차이 만큼 조망권 확보
            # 양옆2개씩의 빌딩 중 가장 높은 높이 찾기
            hightest_around = arounds[0]
            for around in arounds:
                if hightest_around < around:
                    hightest_around = around
            cnt_view += now - hightest_around

    print(f"#{test_case} {cnt_view}")



