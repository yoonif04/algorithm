def comb(i):
    if i == M:
        comb_result.append(c[:])
    else:
        for j in range(1, len(chicken) + 1):
            if i == 0 or (not used[j] and c[i-1] < j):
                used[j] = 1
                c[i] = j
                comb(i+1)
                used[j] = 0


# NxN 도시, M개의 치킨 고르기
N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))
result = 999999
house = []      # 집의 좌표
chicken = []      # 치킨집의 좌표

# 집의 좌표, 치킨집의 좌표 담기
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

used = [0] * (len(chicken) + 1)
c = [0] * M
comb_result = []    # 치킨집 M개 뽑은 조합
comb(0)

# 조합에서 치킨집 인덱스리스트 조합 하나씩 꺼내기
for idx_list in comb_result:
    dist = 0    # 전체 거리
    # 집 하나씩 조합에 대해 거리 찾기
    for h in house:
        chi_dist = 999
        # 인덱스리스트에 속한 치킨집 하나씩 거리 구하기
        for idx in idx_list:
            chi_dist = min(chi_dist, abs(h[0]-chicken[idx-1][0]) + abs(h[1] - chicken[idx-1][1]))
        dist += chi_dist
    result = min(result, dist)

print(result)