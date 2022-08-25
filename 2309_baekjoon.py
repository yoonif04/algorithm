n = 9
height = []
for _ in range(n):
    h = int(input())
    height.append(h)
# 키 차이(100보다 얼마나 높아졌는지)
diff = sum(height) - 100

# 두 키의 합이 diff만큼 되는 경우 찾아서 빼기
flag = False
for i in range(n-1):
    for j in range(i+1, n):
        if height[i] + height[j] == diff:
            height[i] = height[j] = 0
            flag = True
            break
    if flag:
        break

# 정렬 후 출력
for i in range(n-1):
    minIdx = i
    for j in range(i+1, n):
        if height[minIdx] > height[j]:
            minIdx = j
    height[i], height[minIdx] = height[minIdx], height[i]

for h in height:
    if h:
        print(h)
