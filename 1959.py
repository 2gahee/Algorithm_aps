import sys
sys.stdin=open('input (9).txt')

T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    if N > M:
        max = N
        max_lst = A_lst
        min = M
        min_lst = B_lst

    elif N < M:
        max = M
        max_lst = B_lst
        min = N
        min_lst = A_lst

    elif N == M:
        for i in range(N):
            for j in range(M):
                max_total = A_lst[i] * B_lst[j]


    max_total = float('-inf')
    for i in range(0, max-min+1):  #max_lst의 시작점(기준점)
        total = 0                    #max_lst시작점 바뀔때마다 total 초기화
        for k in range(0, min):       #시작점에서 min_lst길이만큼 더해줘야함
            multi = max_lst[i+k] * min_lst[k]
            total += multi
        if total > max_total:  #total값 중 음수도 포함되어있므로 for문 다 돈후 최대totL구하기
            max_total = total

    print(f'#{tc} {max_total}')


