def prefix(node):
    if node != ".":
        print(node, end="")
        prefix(left[ord(node)-ord('A')])
        prefix(right[ord(node)-ord('A')])


def infix(node):
    if node != ".":
        infix(left[ord(node) - ord('A')])
        print(node, end="")
        infix(right[ord(node) - ord('A')])


def postfix(node):
    if node != ".":
        postfix(left[ord(node) - ord('A')])
        postfix(right[ord(node) - ord('A')])
        print(node, end="")
        return node


N = int(input())
left = [0] * N
right = [0] * N

for _ in range(N):
    node, l, r = input().split()
    num = ord(node) - ord('A')
    left[num] = l
    right[num] = r


prefix('A')
print()
infix('A')
print()
postfix('A')
print()