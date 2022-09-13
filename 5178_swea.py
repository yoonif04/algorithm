# 5178. 노드의 합
T = int(input())
for tc in range(1, T+1):
    # N:노드의 개수, M:리프노드의 개수, L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    # tree 정보
    tree = [0] * (N+1)  # 1~N번 노드

    # 리프 노드의 정보를 받아서 채우기
    for _ in range(M):
        leaf_node, leaf_val = map(int, input().split())
        tree[leaf_node] = leaf_val

    # 나머지 노드 채우기
    for i in range(N, 0, -1):
        # 비어있다면(리프노드 아니라면)
        if not tree[i]:
            # 왼쪽자식 존재한다면 값 더하기
            if i*2 <= N:
                tree[i] += tree[i*2]
            # 오른쪽자식 존재한다면 값 더하기
            if i*2+1 <= N:
                tree[i] += tree[i*2+1]

    print(f"#{tc} {tree[L]}")