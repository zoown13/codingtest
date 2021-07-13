count = 0


def solution(numbers, target):
    answer = 0

    init_num = numbers.pop()

    DFS(numbers, init_num, target, '+')
    # print(count)
    DFS(numbers, -init_num, target, '-')

    answer = count

    return answer


def DFS(numbers, sum_value, target, orders):
    global count

    if len(numbers) == 0 and sum_value == target:
        count += 1
        # print(orders)

    if len(numbers) == 0:
        return

    val = numbers.pop()

    for operand in ['+', '-']:
        if operand == '+':
            DFS(numbers, sum_value + val, target, orders + '+')
        else:
            DFS(numbers, sum_value - val, target, orders + '-')

    numbers.append(val)
    return


'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

'''