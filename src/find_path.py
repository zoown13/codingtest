found = 0
N = 0


def findpath(startX, startY, map_info, visited):
    global found
    if found:
        return

    if map_info[startX][startY] == 3:
        found = 1
        return

    visited[startX][startY] = 1

    # left
    if startY - 1 >= 0:
        if map_info[startX][startY - 1] in [0, 3] and visited[startX][startY - 1] == 0:
            findpath(startX, startY - 1, map_info, visited)
    # right
    if startY + 1 < N:
        if map_info[startX][startY + 1] in [0, 3] and visited[startX][startY + 1] == 0:
            findpath(startX, startY + 1, map_info, visited)
    # up
    if startX - 1 >= 0:
        if map_info[startX - 1][startY] in [0, 3] and visited[startX - 1][startY] == 0:
            findpath(startX - 1, startY, map_info, visited)
    # down
    if startX + 1 < N:
        if map_info[startX + 1][startY] in [0, 3] and visited[startX + 1][startY] == 0:
            findpath(startX + 1, startY, map_info, visited)

    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input().strip())

    map_info = [[] for _ in range(N)]  # Initializing a map
    visited = [[] for _ in range(N)]  # Initializing a visited map

    X, Y = 0, 0  # Initializing start x,y

    # construct map and visited map
    for i in range(N):
        info = input().strip()
        for j in range(N):
            map_info[i].append(int(info[j]))
            visited[i].append(0)
            if int(info[j]) == 2:
                X, Y = i, j

    findpath(X, Y, map_info, visited)

    if found == 1:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))

    found = 0
