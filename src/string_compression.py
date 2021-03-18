def solution(s):
    answer = 0
    minimumLength = len(s)

    i = 0
    unit = 1
    j = unit + i
    start = 0
    end = 0
    temp = s

    while len(s) > unit:

        if s[i:j] == s[j:j+unit]:
            end = j+unit

        else:
            if end == 0:
                start = j
            else:
                temp = temp.replace(s[start:end], str(int((end - start)/unit))+s[i:j])
                start = j
                end = 0

        i = j
        j = i + unit
        if j > len(s):
            unit += 1

            if minimumLength > len(temp):
                minimumLength = len(temp)

            i = 0
            j = unit + i
            start = 0
            end = 0
            temp = s

    answer = minimumLength

    return answer


if __name__ == '__main__':
    solution('xababcdcdababcdcd')