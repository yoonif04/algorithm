def same_reverse(str1):
    reverse = ""
    for i in range(len(str1)-1, -1, -1):
        reverse += str1[i]
    if str1 == reverse:
        return str1
    else:
        return False

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    sentence = [input() for _ in range(N)]
    result = ""
    # 행 순회
    for i in range(N):     # 행
        for j in range(N-M+1):   # 시작열
            same = same_reverse(sentence[i][j:j+M])  # M개
            if same:   # False 아닌 값
                result = same   # 문자열 저장
    # 열 순회
    for j in range(N):
        for i in range(N-M+1):   # 시작 행
            word = ""            # 문자이어붙이기
            for k in range(i, i+M):  # M개 만큼
                word += sentence[k][j]
            same = same_reverse(word)
            if same:   # False 아닌 값
                result = same   # 문자열 저장

    print(f"#{test_case} {result}")