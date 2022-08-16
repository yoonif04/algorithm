import sys
sys.stdin = open("sample_input.txt", "r")
def BruteForce(t, p):
    idx_t, idx_p = 0, 0
    cnt = 0
    while idx_t < len(t):
        if t[idx_t] != p[idx_p]:
            idx_t -= idx_p
            idx_p = -1
        idx_t += 1
        idx_p += 1
        if idx_p == len(p):
            cnt += 1
            idx_p = 0
    return cnt

T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    cnt = BruteForce(A, B)
    result = len(A) - len(B)*cnt + cnt
    print(f"#{test_case} {result}")