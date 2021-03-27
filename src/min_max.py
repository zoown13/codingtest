def solution():
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        # ///////////////////////////////////////////////////////////////////////////////////
        num_count = int(input())
        num_list = sorted(list(map(int, input().strip().split())))
        min_num = num_list[0]
        max_num = num_list[-1]
        difference = max_num - min_num
        print("#{} {}".format(test_case, difference))
        # ///////////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    solution()