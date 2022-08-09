# List1 : 전기버스
# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())  # 노선 수
for test_case in range(1, T+1):
    # K:이동가능한 정류장수, N:종점번호, M:충전기정류장개수
    K, N, M = map(int, input().split())
    # 충전기 설치된 정류장 정보
    bus_stops = list(map(int, input().split()))
    # cur:커서,이동한 위치 나타냄(충전소), cnt:충전횟수
    cur = cnt = 0
    # 커서가 N-K보다 작을때까지만 확인
    # 커서 N-K라면 -> 종점가기전까지 필요한 충전 완료 -> 충전 필요없음
    while cur < N - K:
        # 충전 가능한지 여부 나타낼 변수
        charge = False
        # 커서+1부터 커서+K 안에 충전소가 존재하는지 파악
        # 가능한 범위에서 가장 먼 충전소를 커서로 이동 -> 최소 충전
        for i in range(cur+1, cur+K+1):
            if i in bus_stops:   # i가 충전기 설치된 곳이라면
                cur = i          # 커서를 i로 옮기고
                charge = True    # charge를 True로
        if charge:    # charge가 True라면
            cnt += 1  # 충전횟수 1 증가
        else:         # charge가 False라면
            cnt = 0   # 충전횟수 0으로 초기화 후 break
            break

    print(f'#{test_case} {cnt}')

# 전기버스 - 교수님 풀이
import sys
sys.stdin = open("sample_input.txt", "r")
def drive(K, N):  # 버스를 운행하는 함수
    # return = 0: 충전소가 제대로 배치X -> 완주X
    # return > 0: 충전소 제대로 배치
    last = 0  # 마지막으로 충전했던 위치
    next = K  # 버스가 최대로 이동한 위치 (초기값은 한번 이동한 상태로)
    count = 0  # 충전 횟수
    # 종점에 도착할 때까지 반복
    while next < N:
        # 버스가 이동한 위치에 충전기가 있나 없나 검사
        # 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을때까지 뒤로 간다
        while stop[next] == 0:
            next -= 1   # 뒤로 이동
            # 뒤로 갔는데 내가 마지막으로 충전한 위치까지 와버렸다면 충전소 제대로 배치X
            if next == last:
                return 0
        # 여기까지 왔다면 충전기 제대로 설치됨
        # 마지막 충전 위치 갱신
        last = next
        # 다음 위치로 이동
        next += K
        # 충전 횟수 증가
        count += 1
    # N보다 next가 크거나 같아졌으니까 완주했음
    return count


T = int(input())
for tc in range(1, T+1):
    # K:이동가능한 정류장수, N:종점번호, M:충전기정류장개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    stop = [0]*N  # 정류장 리스트(1:충전소O, 2:충전소X)
    for x in charge:  # x: 충전소있는 정류장 위치
        stop[x] = 1
    answer = drive(K, N)
    print(f"#{tc} {answer}")