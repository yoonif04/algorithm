def BruteForce(p, t):
    idx_p, idx_t = 0, 0
    cnt = 0   # 패턴 개수 셀 변수
    while idx_t < len(t):
        if t[idx_t] != p[idx_p]:
            idx_t -= idx_p
            idx_p = -1
        idx_t += 1
        idx_p += 1
        if idx_p == len(p):
            cnt += 1
            idx_p = 0  # 0으로 초기화
    return cnt


T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    max_val = 0   # 가장 많이 등장하는 문자 개수 셀 변수
    for word in str1:
        result = BruteForce(word, str2)
        if max_val < result:
            max_val = result
    print(f"#{test_case} {max_val}")