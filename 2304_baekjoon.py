# 기둥 개수
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort()  # 정렬해서 왼쪽부터 등장번호 순서대로
# 가장 높은 창고
highest = max(data, key=lambda x: x[1])
highest_idx = -1
for i in range(N):
    if data[i][1] == highest[1]:
        highest_idx = i

area = highest[1]   # 면적 합 저장할 변수

now = data[0]  # 현재 빌딩
for i in range(highest_idx+1):
    if now[1] <= data[i][1]:
        area += (now[1] * (data[i][0] - now[0]))
        now = data[i]

now = data[-1]  # 현재 빌딩
for i in range(N-1, highest_idx-1, -1):
    if now[1] <= data[i][1]:
        area += (now[1] * (now[0]-data[i][0]))
        now = data[i]

print(area)