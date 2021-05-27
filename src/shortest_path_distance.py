from collections import deque
# 과연 BFS 접근시 항상 짧은 경로를 먼저 찾을 수 있는가?


def count_distance(startX, startY):
    q = deque()
    q.append((startX, startY))
    visited.append((startX, startY))

    def in_bound(x, y):
        return N > x >= 0 and N > y >= 0 and map_info[x][y] in [0, 3] and (x, y) not in visited

    while q:
        coordinate = q.popleft()
        x, y = coordinate[0], coordinate[1]

        # up
        if in_bound(x - 1, y):
            visited.append((x - 1, y))
            if map_info[x - 1][y] == 3:
                distance[x - 1][y] = distance[x][y]
                return
            else:
                q.append((x - 1, y))
                distance[x - 1][y] = distance[x][y] + 1

        # down
        if in_bound(x + 1, y):
            visited.append((x + 1, y))
            if map_info[x + 1][y] == 3:
                distance[x + 1][y] = distance[x][y]
                return
            else:
                q.append((x + 1, y))
                distance[x + 1][y] = distance[x][y] + 1

        # left
        if in_bound(x, y - 1):
            visited.append((x, y - 1))
            if map_info[x][y - 1] == 3:
                distance[x][y - 1] = distance[x][y]
                return
            else:
                q.append((x, y - 1))
                distance[x][y - 1] = distance[x][y] + 1

            # right
        if in_bound(x, y + 1):
            visited.append((x, y + 1))
            if map_info[x][y + 1] == 3:
                distance[x][y + 1] = distance[x][y]
                return
            else:
                q.append((x, y + 1))
                distance[x][y + 1] = distance[x][y] + 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input().strip())
    distance = [[0] * N for _ in range(N)]
    map_info = [list(map(int, input().strip())) for _ in range(N)]
    visited = []

    startX, startY = 0, 0
    goalX, goalY = 0, 0

    for i in range(N):
        for j in range(N):
            if map_info[i][j] == 2:
                startX, startY = i, j
            elif map_info[i][j] == 3:
                goalX, goalY = i, j

    count_distance(startX, startY)

    print("#{} {}".format(test_case, distance[goalX][goalY]))