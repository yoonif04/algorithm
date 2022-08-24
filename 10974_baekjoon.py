# 순열
def npr(i):
    if i == n:   # n과 같아지면 출력
        for num in s:
            print(num, end=" ")
        print()
    else:
        # j번째 자리 구하기 - 1부터 n인덱스
        for j in range(1, n+1):
            if not visited[j]:  # 방문하지 않았으면
                # 방문처리, 값 추가 후 다음으로
                visited[j] = True
                s.append(j)
                npr(i+1)
                # 원상복구
                s.pop()
                visited[j] = False


n = int(input())
s = []
visited = [False] * (n+1)
npr(0)