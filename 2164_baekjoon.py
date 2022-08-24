# 시간 초과
# n = int(input())
#
# q = [x for x in range(n+1)]     # 0~n을 넣고 시작
# front = 0
# rear = n    #
#
# while front + 1 != rear:    # 큐의 길이 1일때까지
#     # 제거
#     front = (front + 1) % (n+1)
#     # 제거 후 뒤에 넣기
#     front = (front + 1) % (n+1)
#     rear = (rear + 1) % (n+1)
#     q[rear] = q[front]
#
# print(q[front+1])


from collections import deque
n = int(input())
q = deque([x for x in range(1, n+1)])
while len(q) != 1:
    q.popleft()     # 제거
    v = q.popleft()
    q.append(v)
print(q[0])