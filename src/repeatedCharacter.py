T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_str = input()
    processed_str = []
    for i in range(len(input_str)):
        if len(processed_str) != 0:
            if processed_str[-1] == input_str[i]:
                processed_str.pop()
            else:
                processed_str.append(input_str[i])

        else:
            processed_str.append(input_str[i])
    print("#{} {}".format(test_case, len(processed_str)))
