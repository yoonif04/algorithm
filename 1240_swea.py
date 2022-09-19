# 1240. 단순 2진 암호코드
import sys
sys.stdin = open("input.txt", "r")

code_dict = {
    '0001101': 0, '0011001': 1,
    '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]

    code_word = ''
    for i in range(N):
        # 0이 아니면 암호부분이다
        if sum(map(int, code[i])) != 0:
            for j in range(M-1, -1, -1):
                # 암호의 끝이 1로 끝남
                if code[i][j] == '1':
                    # 56개
                    code_word = code[i][j-55:j+1]
                    break

    # 7개씩 끊고, 암호 변환
    code_word_list = [code_dict[code_word[i: i+7]] for i in range(0, 56, 7)]

    odd = [code_word_list[x] for x in range(0, 8, 2)]
    even = [code_word_list[x] for x in range(1, 8, 2)]

    answer = sum(odd) * 3 + sum(even)
    print(f"#{tc}", end=" ")
    if answer % 10 == 0:
        print(sum(code_word_list))
    else:
        print(0)