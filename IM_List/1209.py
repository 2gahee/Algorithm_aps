import sys
sys.stdin = open('input (9).txt')

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    count=0
    max_cnt = 0
    #행 최대값
    for i in range(100):
        count = 0
        for j in range(100):
            count += arr[i][j]
            if count > max_cnt:
                max_cnt = count
    #열 최대값
    for j in range(100):
        count = 0
        for i in range(100):
            count += arr[i][j]
            if count > max_cnt:
                max_cnt = count

    #대각선 \ 최대값
    count = 0  #count초기화 잊지말기
    for i in range(100):
        count += arr[i][i]
        if count > max_cnt:
            max_cnt = count

    #대각선 / 최대값
    count = 0  #count초기화 잊지말기
    for i in range(100):
        count += arr[i][99-i]
        if count > max_cnt:
            max_cnt = count

    print(f'#{tc} {max_cnt}')