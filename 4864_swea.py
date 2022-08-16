def BruteForce(p, t):
    idx_p, idx_t = 0, 0
    while idx_p < len(p) and idx_t < len(t):
        if t[idx_t] != p[idx_p]:
            idx_t -= idx_p
            idx_p = -1
        idx_t += 1
        idx_p += 1
    if idx_p == len(p):
        return 1
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f"#{test_case} {BruteForce(str1, str2)}")