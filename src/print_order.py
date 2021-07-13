def solution(priorities, location):
    answer = 0
    orders = [i for i in range(len(priorities))]

    # print(orders)
    while True:
        changed = False
        for i in range(len(orders)):
            j = orders.index(i)
            after_orders = orders[j + 1:]
            # print(after_orders)
            for index in after_orders:
                if priorities[i] < priorities[index]:
                    orders.append(i)
                    orders.remove(i)
                    changed = True
            # print(orders)
        if not changed:
            break

    answer = orders.index(location) + 1
    # print(answer)

    return answer


'''

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''