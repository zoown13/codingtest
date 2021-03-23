import re


def solution():
    input_count = int(input())
    user_input = list(input() for _ in range(input_count))

    min_time = "24:00"
    max_time = str()

    for time in user_input:
        pattern = r"[0-9][0-9]:[0-9][0-9]"
        matchedList = re.findall(pattern, time)
        if matchedList:
            if max_time < matchedList[0]:
                max_time = matchedList[0]
            if min_time > matchedList[1]:
                min_time = matchedList[1]

    if min_time < max_time:
        print("{0} ~ {1}".format(max_time, min_time))
    else:
        print("-1")

if __name__ == '__main__':
    solution()