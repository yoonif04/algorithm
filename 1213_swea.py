def BruteForce(p, t):
    idx_t, idx_p = 0, 0   # t,p의 인덱스
    cnt = 0  # 개수
    while idx_t < len(t):
        if t[idx_t] != p[idx_p]:
            idx_t -= idx_p
            idx_p = -1
        idx_t += 1
        idx_p += 1
        # 패턴 인덱스가 패턴 길이와 같으면(존재) -> 개수 증가, 인덱스0으로
        if idx_p == len(p):
            cnt += 1
            idx_p = 0
    return cnt

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    pattern = input()
    sentence = input()
    cnt = BruteForce(pattern, sentence)
    print(f"#{tc} {cnt}")