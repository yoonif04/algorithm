import sys
input = sys.stdin.readline

N = int(input())
# 각 숫자를 셀 변수
cnt = [0]*10001
# 각 숫자를 입력받아 해당 인덱스의 값 증가시키기
for _ in range(N):
    cnt[int(input())] += 1

# 1부터 N까지의 숫자를 0이아니면, 개수만큼 출력
for i in range(10001):
    for j in range(cnt[i]):
        print(i)