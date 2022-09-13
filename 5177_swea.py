# 5177. 이진 힙
T = int(input())
for tc in range(1, T + 1):
    # N: 노드 개수
    N = int(input())
    tree = [0] * (N + 1)  # 1~N번 노드
    nums = list(map(int, input().split()))

    tree[1] = nums[0]  # 1번노드 값
    # 2번노드부터 N번 노드까지 값 채우기
    for i in range(2, N + 1):
        tree[i] = nums[i - 1]
        # 자식이 더 작으면 바꾸기
        while tree[i//2] > tree[i]:
            tree[i//2], tree[i] = tree[i], tree[i//2]
            i //= 2     # 다음 조상도 검토

    sum_val = 0
    node = N  # 마지막 노드에서 시작
    # 노드가 0이 아닐 때까지
    while node:
        node //= 2  # 부모 번호로 바꾸기
        sum_val += tree[node]
    print(f"#{tc} {sum_val}")
