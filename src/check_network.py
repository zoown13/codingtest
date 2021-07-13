from collections import deque


visited = set()


def solution(n, computers):
    answer = 0
    unvisited_network = [0]
    while unvisited_network:
        answer += 1
        network = unvisited_network.pop()
        unvisited_network = BFS(n, computers, network)

    return answer


def BFS(n, computers, i):
    q = deque(index for index, connected in enumerate(computers[i]) if connected == 1 and index != i)
    global visited
    visited.add(i)
    while q:
        computer = q.popleft()
        visited.add(computer)

        for computer_num, connected in enumerate(computers[computer]):
            if computer_num != computer and connected == 1 and computer_num not in visited:
                q.append(computer_num)

    unvisited = []

    for i in range(n):
        if i not in visited:
            unvisited.append(i)
            break

    return unvisited

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))