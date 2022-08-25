N, K = map(int, input().split())
# 여학생, 남학생 학년 정보
grade_0 = [0] * 7   # 여학생
grade_1 = [0] * 7   # 남학생

for _ in range(N):
    gender, grade = map(int, input().split())
    if gender:  # 남학생이면
        grade_1[grade] += 1
    else:
        grade_0[grade] += 1
room = 0
for num in grade_0:
    if num % K:  # 0이 아니면
       room += num//K+1
    else:
        room += num // K

for num in grade_1:
    if num % K:  # 0이 아니면
        room += num // K + 1
    else:
        room += num // K
print(room)
