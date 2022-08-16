import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = 5
    # 빈 공간을 만들어서 문자를 채우기
    blank_list = [[""]*15 for _ in range(N)]
    text = [list(input()) for _ in range(N)]
    # 빈 공간에 문자 넣기
    for i in range(N):
        for j in range(len(text[i])):
            blank_list[i][j] = text[i][j]
    # 문자 출력 - 공백은 무시하고
    print(f"#{test_case}", end=" ")
    for i in range(15):
        for j in range(N):
            if blank_list[j][i] != "":
                print(blank_list[j][i], end="")
    print()