# 5097. 회전
T = int(input())
for tc in range(1, T + 1):
    # N:숫자개수, M:작업횟수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))  # 숫자 정보
    front = 0  # 첫번째를 가리킬 변수
    while M > 0:
        front = (front + 1) % N  # 다음을 가리킴
        M -= 1

    print(f"#{tc} {nums[front]}")