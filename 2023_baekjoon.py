def is_prime(n):
    if n < 2:
        return False
    else:
        m = int((n+1)**0.5)
        for i in range(2, m):
            if n % i == 0:
                return False
        return True


n = int(input())    # 자리수

# 한자리의 소수 목록
# sosu_1 = [2, 3, 5, 7]   # 첫번째 될 수 있는 수
nums = [1, 3, 7, 9]     # 뒤에 붙을 수 있는 수
# result = [[]]*n
# 위는 얕은 복사
result = [[2, 3, 5, 7], [], [], [], [], [], [], []]

# n-1번 반복 - 1자리채워져있음
for i in range(n-1):
    # i+1자리의 길이만큼 반복
    for j in range(len(result[i])):
        # 뒤에 붙을 수 있는 수 만큼 반복
        for num in nums:
            # 새로운 수 = 가능한 수 * 10에 뒤에 붙을 수 있는 수 더한것
            new = result[i][j]*10 + num
            # 소수라면 추가
            if is_prime(new):
                result[i+1].append(new)

for special in result[n-1]:
    print(special)
