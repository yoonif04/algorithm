N = int(input())    # 수열의 길이
nums = list(map(int, input().split()))
up = [0] * N    # 증가 저장할 변수
down = [0] * N  # 감소 저장할 변수

max_cnt = cnt_up = cnt_down = 0
for i in range(1, N):
    if nums[i] >= nums[i-1]:
        cnt_up += 1
        if cnt_up > max_cnt:
            max_cnt = cnt_up
    else:
        cnt_up = 0
    if nums[i] <= nums[i-1]:
        cnt_down += 1
        if cnt_down > max_cnt:
            max_cnt = cnt_down
    else:
        cnt_down = 0
# 구간을 구해야 하므로 1 증가해서 출력
print(max_cnt + 1)