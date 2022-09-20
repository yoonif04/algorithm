import sys
sys.stdin = open("sample_input.txt", "r")
# 2진수로 바꿀 정보가 담긴 딕셔너리
change_bi = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
# 0~9까지의 암호의 비율
code = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 중복 제거
    numbers = sorted(list(set([input()[:M] for _ in range(N)])))
    numbers.pop(0)  # 0만 있는 행 제거

    result = 0  # 결과값
    visited = []  # 암호 중복여부 찾기

    # 암호 순회하면서
    for x in range(len(numbers)):
        change = ""
        # 이진수로 바꾸기
        for y in range(len(numbers[x])):
            change += change_bi[numbers[x][y]]
        # 오른쪽 0 제거
        change = change.rstrip("0")

        # 8자리 암호를 담을 변수
        password = []

        # 비율 나타내기, 0 1 0 1 의 개수세기
        ratio = [0] * 4
        # 이진수의 오른쪽 끝부터 비율 찾기
        for i in range(len(change) - 1, -1, -1):
            # 이진수 값이 1이고 왼쪽 인덱스가 아직 0이라면
            if change[i] == '1' and ratio[2] == 0:
                ratio[3] += 1
            elif change[i] == '0' and ratio[1] == 0:
                ratio[2] += 1
            elif change[i] == '1' and ratio[0] == 0:
                ratio[1] += 1
            # 이진수 값이 0이라면
            elif change[i] == '0':
                # 왼쪽 인덱스가 1이라면 (다른 암호가 존재할 때 시작 직전까지 미리 이동)
                if change[i - 1] == '1':
                    n = min(ratio[1], ratio[2], ratio[3])  # 비율 나눠줄 수
                    # 비율이 의미하는 암호 입력
                    password.append(code[ratio[1] // n, ratio[2] // n, ratio[3] // n])
                    ratio[1] = ratio[2] = ratio[3] = 0  # 비율 초기화

                    # 길이가 8이라면 암호완성
                    if len(password) == 8:
                        # decimal_num_li의 마지막 인덱스가 첫번째 암호, 1번 인덱스부터 세기
                        odd = [password[x] for x in range(1, 8, 2)]
                        even = [password[x] for x in range(0, 8, 2)]
                        # 홀수 *3 + 짝수가 10의 배수이면
                        if (sum(odd) * 3 + sum(even)) % 10 == 0:
                            # 이미 있는 암호가 아니라면
                            if password not in visited:
                                # 결과값 더하고 visited에 저장해놓기
                                result += sum(password)
                                visited.append(password)
                        password = []  # 초기화

    print(f"#{tc} {result}")
