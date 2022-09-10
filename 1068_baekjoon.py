def dfs(r_num, tree):
    tree[r_num] = -2    # 지우기
    # 트리를 순회하면서
    for i in range(N):
        # 지울 번호를 부모로 갖고 있으면 재귀함수로 보내서 지우기
        if r_num == tree[i]:
            dfs(i, tree)


N = int(input())    # 노드의 개수
tree = list(map(int, input().split()))
r = int(input())    # 지울 노드
cnt = 0     # 리프노드 개수를 셀 변수
dfs(r, tree)
# 트리 순회하면서
for i in range(N):
    # 지워진 노드가 아니고 부모노드가 아닌경우 -> 리프노드
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)