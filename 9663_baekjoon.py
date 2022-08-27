import sys
N = int(sys.stdin.readline())
queen = [0]*N
result = 0


def check(x):
    for i in range(x):
        # 행 - 인덱스 -> 동일한 경우 이미 배제되어있음
        # 열이 동일하거나 대각선이라면
        # 대각선: 행차이와 열차이 값 동일한 경우
        if queen[x] == queen[i] or abs(queen[x]-queen[i]) == x - i:
            return False
    return True


def dfs(x):
    global result
    # x번째 행을 채우기
    # x가 N과 같으면 다 채움
    if x == N:
        result += 1

    else:
        for y in range(N):
            queen[x] = y    # y: 열 값
            # x번째 행, y열 이전행열과 비교
            if check(x):
                dfs(x+1)


dfs(0)
print(result)