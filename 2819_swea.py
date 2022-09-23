# 2819. 격자판의 숫자 이어 붙이기
# 동서남북 방향
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def find(word, si, sj, cnt):
    temp = word
    # cnt가 7이면 숫자 완성
    if cnt == 7:
        if word not in result:
            result.append(word)
        return
    else:
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            # 범위 내라면
            if 0 <= ni < N and 0 <= nj < N:
                find(word + nums[ni][nj], ni, nj, cnt + 1)
                word = temp     # 초기화


T = int(input())
for tc in range(1, T+1):
    N = 4
    nums = [list(input().split()) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            find(nums[i][j], i, j, 1)
    print(f"#{tc} {len(result)}")
