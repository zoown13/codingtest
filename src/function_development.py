

def solution():
    answer = []
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    periods = []

    for i in range(len(progresses)):
        remain = 100-progresses[i]
        duration = int(remain / speeds[i])
        if remain % speeds[i] != 0:
            duration = duration + 1
        periods.append(duration)

    print(periods)

    max_period = periods[0]
    count = 1

    for i in range(1, len(periods)):
        if max_period < periods[i]:
            max_period = periods[i]
            answer.append(count)
            count = 1
        else:
            count = count + 1

    answer.append(count)
    print(answer)

    return answer


if __name__ == '__main__':
    solution()