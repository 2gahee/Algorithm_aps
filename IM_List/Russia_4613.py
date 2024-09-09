import sys
sys.stdin = open('Russia_input.txt')
T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr =[list(input()) for _ in range(N)]
    w_cnt = 0
    b_cnt = 0
    r_cnt = 0
    min_cnt=10000
    for wi in range(N-2):
        for j in range(M):
            if arr[wi][j] != 'W':
                w_cnt += 1
        b_cnt=0
        for bi in range(wi+1, N-1):
            for j in range(M):
                if arr[bi][j] != 'B':
                    b_cnt += 1
            r_cnt=0
            for ri in range(bi+1, N):
                for j in range(M):
                    if arr[ri][j] != 'R':
                        r_cnt +=1

            if w_cnt+b_cnt+r_cnt < min_cnt:
                min_cnt = w_cnt+b_cnt+r_cnt

    print(f'#{tc} {min_cnt}')


