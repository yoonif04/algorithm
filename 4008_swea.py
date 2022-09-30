# 4008. [모의 SW 역량테스트] 숫자 만들기
# i번째 계산, now는 현재 값
def perm(i, now):
    global min_v, max_v
    # 연산 횟수 N-1
    if i == N - 1:
        # 최소값보다 작으면 갱신, 최대값보다 크면 갱신
        if now < min_v:
            min_v = now
        if now > max_v:
            max_v = now
    else:
        # 연산개수 4개
        for j in range(4):
            # 연산가능한 횟수 남아있으면
            if op_num[j] > 0:
                op_num[j] -= 1  # 횟수 하나 차감
                # 인덱스별 연산으로 다음 숫자 만들기
                if j == 0:
                    new = now + nums[i + 1]
                elif j == 1:
                    new = now - nums[i + 1]
                elif j == 2:
                    new = now * nums[i + 1]
                elif j == 3:
                    new = int(now / nums[i + 1])
                # 다음연산으로 숫자 보내기
                perm(i + 1, new)
                # 횟수 다시 추가
                op_num[j] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    op_num = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_v = 100000000
    max_v = -100000000
    perm(0, nums[0])
    print(f"#{tc} {max_v - min_v}")