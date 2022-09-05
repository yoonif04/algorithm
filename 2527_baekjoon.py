# 메모리 초과
def find_common(p, l):
    # 색칠된 2차원 리스트 정보, 길이를 받아서
    # 공통부분의 특성을 반환하는 함수
    # 리스트를 순회하면서 2로 색칠된 곳의
    # 가로길이, 세로길이 찾기
    cnt_width = 0
    cnt_height = 0
    # 가로길이 찾기
    for i in range(l):
        for j in range(l):
            # 2라면 길이 늘리기
            if p[i][j] == 2:
                cnt_width += 1
        # 가로길이가 0이상이면 찾기완료
        if cnt_width > 0:
            break
    # 세로길이 찾기
    for j in range(l):
        for i in range(l):
            # 2라면 길이 늘리기
            if p[i][j] == 2:
                cnt_height += 1
        # 세로길이가 0이상이면 찾기완료
        if cnt_height > 0:
            break
    # 공통부분의 특성 구하기
    if cnt_width > 1 and cnt_height > 1:
        return "a"
    elif cnt_width > 1 or cnt_height > 1:
        return "b"
    elif cnt_width == 1 or cnt_height == 1:
        return "c"
    else:
        return "d"


for _ in range(4):
    # 첫4개좌표 - 첫번째 직사각형, 뒤4개좌표 - 두번째 직사각형
    square = list(map(int, input().split()))

    # square 정보의 가장 큰 값만큼 paper라는 배경 만들기
    length = max(square) + 1
    paper = [[0]*length for _ in range(length) ]

    # paper에 색칠하고 겹쳐진 경우 다른색 칠하기
    # 첫번째 직사각형
    for i in range(square[0], square[2]+1):
        for j in range(square[1], square[3]+1):
            paper[i][j] = 1
    # 두번째 직사각형
    for i in range(square[4], square[6]+1):
        for j in range(square[5], square[7]+1):
            # 이미 색칠되어 있는 경우 2 입력
            if paper[i][j] == 1:
                paper[i][j] = 2

    print(find_common(paper, length))