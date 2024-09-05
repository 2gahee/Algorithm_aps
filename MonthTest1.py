# import sys
# sys.stdin=open('algo1_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    now = 0
    ans = N
    food = K
    while now < N-1:
        if food:
            if lst[now]==0:
               now += 1
               food -= 1
            if lst[now]==1:
                food = K
                now += 1
                food -= 1
        else:
            ans = now+1
            break
    print(f'#{tc} {ans}')