# 4366. 정식이의 은행업무
def changeTo10(x, y):
    # 리스트 x, 진수 y
    num = [0] * len(x)
    for i in range(len(x) - 1, -1, -1):
        num[i] = y ** (len(x) - 1 - i)

    sumV = 0
    for i in range(len(x)):
        sumV += num[i] * int(x[i])
    return sumV


T = int(input())
for tc in range(1, T + 1):
    num_2 = list(input())
    num_3 = list(input())

    final_num_2 = []
    final_num_3 = []

    for i in range(len(num_2)):
        if num_2[i] == "0":
            num_2[i] = "1"
            final_num_2.append(changeTo10(num_2, 2))
            num_2[i] = "0"
        else:
            num_2[i] = "0"
            final_num_2.append(changeTo10(num_2, 2))
            num_2[i] = "1"

    for i in range(len(num_3)):
        if num_3[i] == "1":
            num_3[i] = "2"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "0"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "1"
        elif num_3[i] == "2":
            num_3[i] = "1"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "0"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "2"
        elif num_3[i] == "0":
            num_3[i] = "2"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "1"
            final_num_3.append(changeTo10(num_3, 3))
            num_3[i] = "0"

    result = 0
    for num2 in final_num_2:
        for num3 in final_num_3:
            if num2 == num3:
                result = num2
    print(f"#{tc} {result}")
