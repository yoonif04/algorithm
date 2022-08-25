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
    if num:  # 0이 아니면
       room += (num+1)//2

for num in grade_1:
    if num:
        room += (num+1)//2
print(room)