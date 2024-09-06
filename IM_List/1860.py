import sys
sys.stdin =open('input1860.txt')

T=int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 'possible'
    #lst 순회하며
    #각사람이 언제도착하는지이므로
    sort_lst = sorted(lst)
    food = (sort_lst[-1]/M)*K
    for i in range(len(sort_lst)-1):
        if sort_lst[i] < M:
            ans = 'Impossible'
            break
        if sort_lst[-1] < M:
            ans = 'Impossible'
            break
        else:
            K-=1
            if sort_lst[i+1] - sort_lst[i] < M:
                if K == 0:
                    ans = 'Impossible'
                    break
    print('f#{tc} {ans}')


            ##다시풀기