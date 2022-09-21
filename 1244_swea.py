def change(cnt):
    global maxV
    # 교환 횟수만큼 교환 완료
    if cnt == change_num:
        new = "".join(nums)
        if new > maxV:
            maxV = new
        return
    else:
        for i in range(n-1):
            for j in range(i+1, n):
                # 교환
                nums[i], nums[j] = nums[j], nums[i]
                # 바꿨을때의 값, 그리고 교환횟수 정보가 중복인지 확인
                now = "".join(nums)
                # 현재 값, 현재 순서에 대한 정보가 존재하지 않다면
                if now not in visited[cnt]:
                    visited[cnt].append(now)
                    change(cnt+1)
                # 다시 복구
                nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T+1):
    info = list(input().split())
    # 숫자판의 정보
    nums = list(info[0])
    # 교환 횟수
    change_num = int(info[1])
    n = len(nums)   # 숫자판의 길이
    # 인덱스의 번호에 같은 값이 있는지 확인할 변수
    visited = [[] for _ in range(10)]
    maxV = "0"        # 교환 이후의 최대값 저장할 변수
    change(0)
    print(f"#{tc} {maxV}")