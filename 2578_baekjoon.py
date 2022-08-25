# 빙고 정보 받기
bingo = [list(map(int, input().split())) for _ in range(5)]
# 부르는 숫자 정보
calls = [list(map(int, input().split())) for _ in range(5)]

# 숫자 부르고 맞추면 카운트, 빙고 완성되었는지 확인
bingo_row = [0]*5       # 0~4행의 빙고 정보
bingo_col = [0]*5       # 0~4열의 빙고 정보
bingo_cross = [0]*2     # 대각선의 빙고 정보
# 숫자 부를때마다 해당 행, 열의 빙고정보 하나씩 올리고
# 빙고 여부 체크
bingo_num = 0   # 빙고 개수
cnt = 0
for call in calls:
    for num in call:
        cnt += 1
        # 행열 순회하면서 해당 숫자의 행,열 인덱스 찾기
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    bingo_row[i] += 1
                    bingo_col[j] += 1
                    if i == j:
                        bingo_cross[0] += 1
                    if j == 5-i-1:
                        bingo_cross[1] += 1
        bingo_num = 0   # 빙고 개수 초기화
        for i in range(5):
            if bingo_row[i] == 5:
                bingo_num += 1
            if bingo_col[i] == 5:
                bingo_num += 1
        if bingo_cross[0] == 5:
            bingo_num += 1
        if bingo_cross[1] == 5:
            bingo_num += 1
        if bingo_num >= 3:
            break
    if bingo_num >= 3:
        break
print(cnt)
