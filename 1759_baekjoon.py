def find_password(x):
    # print("단계", x)
    # x번째 단계
    if x == L:
        # 모음이 한개 이상이고 자음이 두개 이상인지 확인하기
        sum_vowel = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            sum_vowel += result.count(vowel)
        sum_consonant = L - sum_vowel
        if sum_vowel >= 1 and sum_consonant >= 2:
            for i in range(L):
                print(result[i], end="")
            print()
    else:
        # C개의 알파벳
        for i in range(C):
            # 방문하지 않았다면
            # 1번째 이상의 자리를 채우는 경우 전의 알파벳보다 큰지 확인
            # 0번째 인덱스인 경우 그냥 진행
            if not visited[i] and (x == 0 or (x >= 1 and result[x-1] < alp[i])):
                visited[i] = 1  # 해당 알파벳의 인덱스를 방문처리
                result[x] = alp[i]  # x번째 자리 암호는 i번째 알파벳
                find_password(x+1)  # 다음으로
                visited[i] = 0  # 방문처리 되돌리기


# L: 암호길이, C: 알파벳개수
L, C = map(int, input().split())
alp = sorted(list(input().split()))     # 알파벳 받아서 정렬
visited = [0]*C
result = [0]*L
find_password(0)
