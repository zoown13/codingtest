T = int(input())

graph = []
visited = []  # actually does not necessary in this problem
found = 0


def find_path(v):
    global found
    visited.append(v)
    if v == dest:
        found = 1
        return
    for vertex in graph[v - 1]:
        find_path(vertex)
        visited.pop()
        if found == 1:
            return


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    vertices, edges = map(int, input().split())

    graph = [[] for _ in range(vertices)] # Initializing a graph
    visited = []
    found = 0

    # making a graph
    for i in range(edges):
        start, end = map(int, input().split())
        graph[start - 1].append(end)

    # path to find
    start, dest = map(int, input().split())

    find_path(start)

    print("#{} {}".format(test_case, found))
