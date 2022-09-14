# 노드 개수가 최대 100,000개이고 유사중위순회에서 호출이 계속됨
# setrecursionlimit() 변경
import sys
sys.setrecursionlimit(100000*10)


# 중위순회
def inorder(n):
    global last
    if n != -1:
        inorder(left[n])
        last = n  # 방문할 때마다 갱신
        inorder(right[n])


# 유사중위순회
def similar(n):
    global last, cnt
    visited[n] = 1  # 방문처리
    # 왼쪽이 존재하고, 방문하지 않았다면
    if left[n] != -1 and not visited[left[n]]:
        cnt += 1    # 이동횟수 증가
        similar(left[n])    # 함수 호출
    # 오른쪽이 존재하고, 방문하지 않았다면
    elif right[n] != -1 and not visited[right[n]]:
        cnt += 1    # 이동횟수 증가
        similar(right[n])   # 함수 호출
    # 현재 노드번호가 last에 저장된 중위순회의 마지막과 같다면 종료
    elif n == last:
        return
    # 부모가 존재한다면(0이 아니라면)
    elif par[n]:
        cnt += 1    # 이동횟수 증가
        similar(par[n])     # 함수 호출


# 노드의 개수
N = int(input())
left = [0] * (N + 1)    # 왼쪽 노드 저장
right = [0] * (N + 1)   # 오른쪽 노드 저장
par = [0] * (N + 1)     # 부모 노드 저장
# 정보 입력받아서 왼쪽, 오른쪽, 부모 노드 입력
for _ in range(N):
    n, l, r = map(int, input().split())
    left[n] = l
    right[n] = r
    # 왼쪽 존재한다면 왼쪽 노드의 부모를 n으로 저장
    if l != -1:
        par[l] = n
    # 오른쪽 존재한다면 오른쪽 노드의 부모를 n으로 저장
    if r != -1:
        par[r] = n

last = 0  # 중위순회 시 마지막 노드 번호
inorder(1)  # 루트는 1로 중위순회 -> last값 갱신됨
visited = [0] * (N + 1)     # 방문여부 기록할 변수
cnt = 0     # 이동횟수 기록할 변수
similar(1)  # 루트 1로 유사중위순회 -> cnt값 갱신됨
print(cnt)
