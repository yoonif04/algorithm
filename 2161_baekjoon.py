from collections import deque
n = int(input())
q = deque([x for x in range(1, n+1)])
while len(q) != 1:
    print(q.popleft(), end=" ")     # 제거
    v = q.popleft()
    q.append(v)
print(q[0])