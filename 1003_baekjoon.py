# 피보나치 함수
# DP

T = int(input())
for _ in range(T):
    num = int(input())
    # 숫자 개수 + 2개 만큼 공간 만들기
    f = [0] * (num + 2)
    # 해당하는 숫자 -> 호출 1번
    f[num] = 1
    # num부터 2까지 1씩 줄여가면서
    for i in range(num, 1, -1):
        # i-1은 i의 수만큼 호출됨
        # i-2는 i의 수만큼 호출됨
        f[i-1] += f[i]
        f[i-2] += f[i]
    print(f[0], f[1])