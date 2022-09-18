def palindrom(li):
    length = len(li)
    for i in range(length//2):
        if li[i] != li[length-1-i]:
            return 0
    return 1


words = input()
print(palindrom(words))