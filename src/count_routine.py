
count = 0

def solution():
    path_length = int(input())
    path_info = list(map(int, list(input())))

    print(path_info)

    find_path(0, path_info, path_length)

    print(count)



def find_path(start, path_info, path_length):
    if start == path_length - 1:
        global count
        count = count + 1
        return

    if path_info[start+1] == 1:
        find_path(start+1, path_info, path_length)

    if start+2 <= path_length - 1:
        if path_info[start + 2] == 1:
            find_path(start + 2, path_info, path_length)


if __name__ == '__main__':
    solution()