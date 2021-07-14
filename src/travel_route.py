routes = []


def solution(tickets):
    answer = []
    airports = set()

    for ticket in tickets:
        airports.add(ticket[0])
        airports.add(ticket[1])

    for index, ticket in enumerate(tickets):
        # 항상 출발하는 공항은 ICN
        if ticket[0] != 'ICN':
            continue
        visited = []
        visited.extend(ticket)
        tickets.remove(ticket)
        DFS(tickets, visited, len(airports))
        tickets.insert(index, ticket)

    routes.sort()
    answer = routes[0]

    return answer


def DFS(tickets, visited, num_airports):
    global routes
    if len(tickets) == 0:
        # list.append(list) 할 경우 shallow copy 되므로 슬라이싱 해줌
        routes.append(visited[:])
        return

    for index, ticket in enumerate(tickets):

        if visited[-1] == ticket[0]:
            tickets.remove(ticket)
            visited.append(ticket[1])

            DFS(tickets, visited, num_airports)

            tickets.insert(index, ticket)
            visited.pop()

    return
