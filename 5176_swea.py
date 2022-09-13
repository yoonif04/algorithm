# 5176. 이진탐색
def inorder(n):
    global num
    if n <= N:
        inorder(n*2)
        tree[n] = num
        num += 1
        inorder(n*2+1)


T = int(input())
for tc in range(1, T+1):
    # N개로 이루어진 완전이진트리
    N = int(input())
    tree = [0] * (N+1)
    # N개 노드의 완전이진트리의 값을 채우기
    num = 1
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")