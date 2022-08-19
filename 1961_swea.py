# 1961번. 숫자 배열 회전
import sys

sys.stdin = open("input.txt", "r")


def rotate(li):
    # list입력받아서 num만큼 90도 회전하기
    # if num == 0:
    #     return li
    # mat = rotate(li, num - 1)  # 사용할 2차원리스트
    new = []  # 새로 생성할 리스트
    for i in range(N):
        row = []  # 새로운 행
        for j in range(N - 1, -1, -1):
            row.append(li[j][i])
        new.append(row)
    return new


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 행렬 크기
    li = [list(input().split()) for _ in range(N)]
    mat1 = rotate(li)
    mat2 = rotate(mat1)
    mat3 = rotate(mat2)
    print(f"#{tc}")
    for i in range(N):
        print("".join(mat1[i]), end=" ")
        print("".join(mat2[i]), end=" ")
        print("".join(mat3[i]), end=" ")
        print()
