w, h = map(int, input().split())
n = int(input())
cutW = [0, w]
cutH = [0, h]

for _ in range(n):
    cut, num = map(int, input().split())
    if cut == 0:
        cutH.append(num)
    else:
        cutW.append(num)

# 가로, 세로 자르는 곳 정렬
for i in range(len(cutH)-1):
    minIdx = i
    for j in range(i, len(cutH)):
        if cutH[minIdx] > cutH[j]:
            minIdx = j
    cutH[minIdx], cutH[i] = cutH[i], cutH[minIdx]
for i in range(len(cutW)-1):
    minIdx = i
    for j in range(i, len(cutW)):
        if cutW[minIdx] > cutW[j]:
            minIdx = j
    cutW[minIdx], cutW[i] = cutW[i], cutW[minIdx]

# 크기 구하기
max_size = 0
for i in range(len(cutH)-1):
    for j in range(len(cutW)-1):
        size = 0
        for x in range(cutH[i], cutH[i+1]):
            for y in range(cutW[j], cutW[j+1]):
                size += 1
        if size > max_size:
            max_size = size
print(max_size)
