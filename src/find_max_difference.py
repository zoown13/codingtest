T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    arr_num, sec_num = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []
    for i in range(arr_num-sec_num+1):
        sum_list.append(sum(num_list[i:i+sec_num]))
    res = sorted(sum_list)
    max_num = res[-1]
    min_num = res[0]
    print("#{} {}".format(test_case, max_num-min_num))