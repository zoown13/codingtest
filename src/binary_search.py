T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    cntA = cntB = 0
    left = 1
    right = P
    while True:
        c = int((left + right)/2)
        cntA = cntA + 1
        if Pa == c:
            break
        elif c > Pa:
            right = c
        else:
            left = c

    left = 1
    right = P

    while True:
        c = int((left + right)/2)
        cntB = cntB + 1
        if Pb == c:
            break
        elif c > Pb:
            right = c
        else:
            left = c

    if cntA > cntB:
        print("#{} B".format(test_case))
    elif cntA < cntB:
        print("#{} A".format(test_case))
    else:
        print("#{} 0".format(test_case))