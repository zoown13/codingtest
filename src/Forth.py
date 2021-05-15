T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = []
    flag = 1
    code = list(input().split())
    for i in range(len(code)-1):
        if code[i].isdigit():
            number.append(int(code[i]))
        else:
            if len(number) >= 2:
                y = number.pop()
                x = number.pop()
                if code[i] == '+':
                    result = x + y
                elif code[i] == '-':
                    result = x - y
                elif code[i] == '*':
                    result = x * y
                elif code[i] == '/':
                    result = x / y
                number.append(result)
            else:
                flag = 0
                break
    if flag and len(number) == 1:
        print("#{} {}".format(test_case, number.pop()))
    else:
        print("#{} error".format(test_case))
