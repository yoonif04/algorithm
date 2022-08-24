import sys
sys.stdin = open("input.txt", "r")
# 암호생성기
for _ in range(1, 11):
    tc = int(input())
    nums = list(map(int, input().split()))  # 8개의 숫자 입력되어있는 큐
    front = 0  # 시작 원소의 위치를 가리킴
    n = 8

    flag = True     # 종료 여부 나타내기
    while flag:
        for i in range(1, 6):
            # i만큼 빼주고 다음 숫자 가리키기
            nums[front] -= i   # 값 감소
            front = (front + 1) % n     # front 가리키는 값 다음으로

            if nums[front-1] <= 0:    # 0보다 작으면
                nums[front-1] = 0     # 0으로 바꾸고 flag False로 바꾸기
                flag = False
                break
    new_password = nums[front:] + nums[0:front]

    print(f"#{tc}", end=" ")
    for password in new_password:
        print(password, end=" ")
    print()


# pop, append 메서드 사용해서 풀이
import sys
sys.stdin = open("input.txt", "r")
for _ in range(1, 11):
    tc = int(input())
    q = list(map(int, input().split()))
    flag = True
    while flag:
        for i in range(1, 6):
            new = q.pop(0) - i
            if new <= 0:
                q.append(0)
                flag = False
                break
            q.append(new)
    print(f"#{tc}", end=" ")
    for num in q:
        print(num, end=" ")
    print()