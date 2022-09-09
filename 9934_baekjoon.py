def get(s, e, k):
    # 시작 끝 같다면 -> 원소 한개
    # s, e: 시작과 끝, k: 레벨
    if s == e:
        tree[k].append(num[s])
        return
    # 중심을 레벨 k위치의 트리에 넣고
    mid = (s + e) // 2
    tree[k].append(num[mid])
    # 왼쪽과 오른쪽을 재귀함수로 반복, 레벨 하나 증가해서
    get(s, mid-1, k+1)
    get(mid+1, e, k+1)


K = int(input())
num = list(map(int, input().split()))
tree = [[] for _ in range(K)]   # 레벨 별 요소들 담을 변수
get(0, len(num)-1, 0)
# 레벨별로 출력
for i in range(K):
    print(*tree[i])
