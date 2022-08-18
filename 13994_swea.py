T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노선 수
    counts = [0] * 1001

    for _ in range(N):
        bus_type, A, B = map(int, input().split())
        counts[B] += 1  # 종점 무조건 정차
        if bus_type == 1:  # 일반 버스 -> 전부 정차
            for i in range(A, B):
                counts[i] += 1
        elif bus_type == 2:
            # 2칸씩 건너뛰어 정차 - 짝수면짝수만, 홀수면 홀수만
            for i in range(A, B, 2):
                counts[i] += 1
        elif bus_type == 3:
            if not A % 2:  # 짝수이면
                for i in range(A, B):
                    if not i % 4:
                        counts[i] += 1
            else:  # 홀수면
                for i in range(A, B):
                    if not i % 3 and i % 10:
                        counts[i] += 1
    # 최대 몇 개의 노선이 같은 정류장에 정차하는지 세기
    max_val = 0
    for i in counts:
        if max_val < i:
            max_val = i
    print(f"#{tc} {max_val}")
