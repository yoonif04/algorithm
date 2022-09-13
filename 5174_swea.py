# 5174. subtree
def find_child(root):
    global cnt
    if root != 0:
        cnt += 1
        find_child(ch1[root])
        find_child(ch2[root])


T = int(input())
for tc in range(1, T + 1):
    # E:간선의 개수, N:찾고자하는 서브트리의 루트번호
    E, N = map(int, input().split())
    # 부모번호를 인덱스로하는 자식 정보를 담을 변수
    ch1 = [0] * (E + 2)  # 노드: 1번 ~ E+1번
    ch2 = [0] * (E + 2)
    arr = list(map(int, input().split()))
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if not ch1[p]:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    find_child(N)
    print(f"#{tc} {cnt}")