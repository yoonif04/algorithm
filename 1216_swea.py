import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    tc = int(input())
    N = 100  # 가로, 세로 길이
    text = [list(input()) for _ in range(N)]

    M = N         # 회문 찾을 길이
    max_len = 0   # 가장 긴 회문의 길이를 저장할 변수
    flag = False  # palindrome 찾았는지 여부
    # 회문 찾을 길이가 0이상이고 flag가 False일 동안 반복
    while M >= 0 and not flag:
        # 행 순회
        for i in range(N):  # 행
            for j in range(N - M + 1):  # 시작열 인덱스
                # 거꾸로 읽었을 때 같으면
                if text[i][j:j + M] == text[i][j:j + M][::-1]:
                    # 팰린드롬 길이가 가장 긴지 비교
                    pal_len = len(text[i][j:j + M])
                    if max_len < pal_len:
                        max_len = pal_len
                        flag = True    # flag를 True로 바꿈
        # 열 순회
        for j in range(N):  # 열
            for i in range(N - M + 1):  # 시작행 인덱스
                word = ""   # 문자이어붙일 변수
                for k in range(i, i + M):  # i부터 M개
                    word += text[k][j]
                # 거꾸로 읽었을 때 같으면 팰린드롬 길이가 가장 긴지 비교
                if word == word[::-1]:
                    if max_len < len(word):
                        max_len = len(word)
                        flag = True    # flag를 True로 바꿈
        M -= 1  # 찾을 길이 감소

    print(f"#{tc} {max_len}")