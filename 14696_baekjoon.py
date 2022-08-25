# 별:4, 동그라미:3, 네모:2, 세모:1

N = int(input())    # 라운드 수
for _ in range(N):
    # A와 B의 딱지 정보
    numsA = list(map(int, input().split()))
    numsB = list(map(int, input().split()))
    # A와 B의 딱지 정보를 미리 세어놓은 변수
    cntA = [0]*5
    cntB = [0]*5

    nA = numsA[0]
    nB = numsB[0]
    for i in range(1, nA+1):
        cntA[numsA[i]] += 1
    for i in range(1, nB+1):
        cntB[numsB[i]] += 1

    # 규칙에 따라 비교
    if cntA[4] > cntB[4]:
        print("A")
    elif cntA[4] < cntB[4]:
        print("B")
    else:
        if cntA[3] > cntB[3]:
            print("A")
        elif cntA[3] < cntB[3]:
            print("B")
        else:
            if cntA[2] > cntB[2]:
                print("A")
            elif cntA[2] < cntB[2]:
                print("B")
            else:
                if cntA[1] > cntB[1]:
                    print("A")
                elif cntA[1] < cntB[1]:
                    print("B")
                else:
                    print("D")