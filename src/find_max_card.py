T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    card_num = int(input())
    cards = input()
    num_dict = dict()
    for i in range(card_num):
        if cards[i] in num_dict:
            num_dict[cards[i]] = num_dict[cards[i]] + 1
        else:
            num_dict[cards[i]] = 1
    res = sorted(num_dict.items(),key=(lambda x: (x[1], x[0])), reverse=True)
    # 정렬시 기준을 여러 조건으로 하려면 튜플 형태로 기준을 순서대로 반환하면됨
    max_card, max_num = res[0]
    print("#{} {} {}".format(test_case,max_card,max_num))
