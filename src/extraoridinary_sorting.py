T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    asc_list = sorted(N_list, reverse=False)
    dsc_list = sorted(N_list, reverse=True)

    zipped_list = list(zip(dsc_list, asc_list))

    ret = []

    for i in range(len(N_list) // 2):
        ret.extend(zipped_list[i])

    ret_str = " ".join(str(e) for e in ret)
    print("#{} {}".format(test_case, ret_str))
