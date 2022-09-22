# 5203. 베이비진 게임
def babygin(li, idx):
    # 리스트에서 idx까지 run이나 triplet이 되는지 확인해서 반환
    cnt = [0] * 10  # 0~9까지를 저장할 변수
    # 숫자 등장 횟수 카운트
    for i in range(idx + 1):
        cnt[li[i]] += 1

    # run, triplet이 있는지 확인
    if 3 in cnt:
        return True
    for i in range(8):
        if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    player1 = [nums[x] for x in range(0, 12, 2)]
    player2 = [nums[x] for x in range(1, 12, 2)]

    result = 0
    for i in range(6):
        if babygin(player1, i):
            result = 1
            break
        elif babygin(player2, i):
            result = 2
            break

    print(f"#{tc} {result}")
