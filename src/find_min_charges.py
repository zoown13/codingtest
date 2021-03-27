T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dist, dest, num_station = map(int, input().split())
    station_list = list(map(int, input().split()))
    loc = 0
    charge_count = 0
    start = 0

    while loc + dist < dest:
        avail_range = loc + dist
        avail_station = []
        for station in station_list[start:]:
            if avail_range >= station:
                avail_station.append(station)
        if len(avail_station) > 0:
            loc = avail_station[-1]
            start = station_list.index(loc) + 1
        else:
            charge_count = 0
            break
        charge_count += 1

    print("#{} {}".format(test_case, charge_count))