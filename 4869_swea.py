# 4869. 종이 붙이기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    paper = [0, 1, 3]
    # i-1번째 + i-2번째 * 2
    for i in range(3, (N // 10) + 1):
        paper.append(paper[i - 1] + 2 * paper[i - 2])

    print(f"#{tc} {paper[N // 10]}")
