# 1231. 중위순회
def inorder(n):
    # n이 0이 아니라면 
    if n != 0:
        inorder(left[n])    # 왼쪽 노드번호로 함수호출
        print(chars[n], end="")     # 해당 노드번호의 문자 출력
        inorder(right[n])   # 오른쪽 노드번호로 함수호출


for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)  # 왼쪽 자식 노드번호 담을 변수
    right = [0] * (N+1)     # 오른쪽 자식 노드번호 담을 변수
    chars = [0] * (N+1)     # 노드의 데이터(문자) 담을 변수

    for _ in range(N):
        # 정보를 한번에 입력받기
        info = list(input().split())
        node = int(info[0])     # 노드번호 0번 인덱스
        chr = info[1]       # 문자 1번 인덱스
        chars[node] = chr   # 해당 노드번호에 문자 저장하기
        # info의 길이가 4이상이면 왼쪽, 오른쪽 자식 존재
        if len(info) >= 4:
            l = int(info[2])    # 왼쪽 노드번호
            r = int(info[3])    # 오른쪽 노드번호
            left[node] = l      # 왼쪽 노드번호 저장
            right[node] = r     # 오른쪽 노드번호 저장
        # info의 길이가 3이상이면 왼쪽 자식 존재
        elif len(info) >= 3:
            l = int(info[2])    # 왼쪽 노드번호
            left[node] = l      # 왼쪽 노드번호 저장

    print(f"#{tc}", end=" ")
    # 루트인 1번부터 중위순회
    inorder(1)
    print()