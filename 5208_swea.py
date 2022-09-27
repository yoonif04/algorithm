# 5208. 전기버스2
def move(i, cnt):
    global minV
    # i 인덱스에 있고 움직인 횟수는 cnt
    # i가 정류장 수-1의 인덱스와 같으면 도착
    if i == N - 1:
        cnt -= 1  # 마지막 정류장에 도착한 경우 빼기
        if cnt < minV:
            minV = cnt
    elif cnt > minV:
        return
    else:
        # 1칸부터 i 인덱스에 해당하는 충전량 만큼 이동 가능
        for j in range(1, battery[i] + 1):
            move(i + j, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    info = list(map(int, input().split()))
    N = info[0]  # 정류장 수
    battery = info[1:]  # N-1개의 정류장 별 배터리 용량

    minV = N  # 최소 이동 횟수 N으로
    move(0, 0)
    print(f"#{tc} {minV}")