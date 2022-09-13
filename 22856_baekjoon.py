# 실패
import sys
sys.setrecursionlimit(1000000)
def find_root():
    for i in range(1, N+1):
        if par[i] == 0:
            return i
def inorder(n):
    global last
    if n != -1:
        inorder(left[n])
        last = n
        inorder(right[n])

N = int(input())
# 노드의 왼쪽, 오른쪽, 부모 저장 변수
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)
# 노드의 정보 저장
for _ in range(N):
    n, l, r = map(int, input().split())
    left[n] = l
    right[n] = r
    if l != -1:
        par[l] = n
    if r != -1:
        par[r] = n

cnt = 0     # 이동횟수 셀 변수
now = find_root()     # 루트노드에서 출발
inorder(now)
visited = [0] * (N+1)   # 방문여부 체크 변수
visited[now] = 1
while True:
    # 왼쪽 존재하고, 방문 안했다면 왼쪽으로 이동
    if left[now] != -1 and not visited[left[now]]:
        visited[left[now]] = 1    # 방문처리
        now = left[now]    # 왼쪽으로 이동
        cnt += 1    # 이동횟수 늘리기
    # 오른쪽 존재하고, 방문 안했다면 오른쪽으로 이동
    elif right[now] != -1 and not visited[right[now]]:
        visited[right[now]] = 1
        now = right[now]   # 오른쪽으로 이동
        cnt += 1    # 이동횟수 늘리기
    # 그렇지 않고 부모 노드가 존재한다면, 부모 노드로 이동
    elif par[now] != 0:
        now = par[now]
        cnt += 1
    # 중위순회의 끝과 같다면, 종료
    if now == last:
        break
print(cnt)