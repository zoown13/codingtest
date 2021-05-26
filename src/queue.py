T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    start = 0
    end = N - 1

    for _ in range(M):
        data.append(data[start])
        start = start + 1
        end = end + 1

    print("#{} {}".format(test_case, data[start]))
