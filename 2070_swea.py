T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    print(f"#{test_case}", end=" ")
    if n < m:
        print("<")
    elif n > m:
        print(">")
    else:
        print("=")