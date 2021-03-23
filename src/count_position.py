import copy

count = 0
count_list = []

def solution():
    length = int(input())
    square = list(input() for _ in range(length))
    square_info = []
    print(square)

    for row in square:
        global count
        count = count + row.count('1')
        square_info.append(list(map(int, list(row))))

    count_list.append(count)

    for side_len in range(1, length):
        temp = copy.deepcopy(square_info)
        num = 0
        for i in range(side_len, length):
            for j in range(side_len, length):
                left = temp[i][j - 1]
                left_up = temp[i - 1][j - 1]
                up = temp[i - 1][j]

                if left == 1 and left_up == 1 and up == 1 and temp[i][j] == 1:
                    square_info[i][j] = 1
                    num = num + 1

                else:
                    square_info[i][j] = 0

        count_list.append(num)

    print("total: {}".format(sum(count_list)))
    for num in range(len(count_list)):
        if count_list[num] != 0:
            print("size[{}]: {}".format(num+1, count_list[num]))





if __name__ == '__main__':
    solution()