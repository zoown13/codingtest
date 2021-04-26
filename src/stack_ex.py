import queue

stack = []
count_list = []


def count_way(dest):
    v = 10
    stack.append(v)
    length = sum(stack)

    if length > dest:
        stack.pop()
        return
    elif length == dest:
        count_list.append(list(stack))
        stack.pop()
        return
    else:
        count_way(dest)
        stack.pop()

    v = 20
    stack.append(v)
    length = sum(stack)
    if length > dest:
        stack.pop()
        return
    elif length == dest:
        count_list.append(list(stack))
        stack.pop()
        return
    else:
        count_way(dest)
        stack.pop()


def GetCount(dest):
    if dest == N:
        return 1
    if dest > N:
        return 0
    return GetCount(dest+10) + GetCount(dest+20)*2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    count_way(N)
    count = 0
    for elem in count_list:
        if 20 in elem:
            x = elem.count(20)
            count = count + 2**x
        else:
            count = count + 1
    count_list = []
    print("#{} {}".format(test_case, count))
    print("#{} {}".format(test_case, GetCount(0)))