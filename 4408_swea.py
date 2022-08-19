# 4408번. 자기 방으로 돌아가기
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 돌아가야 할 학생들의 수
    rooms = [0] * 401   # 400개의 방
    # N번 반복
    for _ in range(N):
        # 현재 방, 돌아갈 방
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start

        if start % 2 == 0:   # 현재 방 짝수라면
            rooms[start-1] += 1
        if end % 2:    # 도착 방 홀수라면
            rooms[end+1] += 1

        # 현재방부터 돌아갈 방까지 1씩 증가
        for i in range(start, end + 1):
            rooms[i] += 1

    # rooms에서 가장 큰 수 찾기
    max_val = 0
    for val in rooms:
        if max_val < val:
            max_val = val
    print(f"#{tc} {max_val}")