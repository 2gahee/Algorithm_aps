import sys
sys.stdin=open('switch_sample_in.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    before_lst = list(map(int, input().split()))
    after_lst = list(map(int, input().split()))
    # print(before_lst)
    # before_lst[2:N]= [10] * (N-2)
    # print(before_lst)
    count = 0
    for i in range(len(before_lst)):
        if before_lst[i] != after_lst[i]:
            count += 1
            for j in range(i,N):
                if before_lst[j] == 0:
                    before_lst[j] = 1
                elif before_lst[j] == 1:
                    before_lst[j] = 0
        if before_lst == after_lst:  # 두 리스트의  모든 원소가 같으면 멈춤
            break

    print(f'#{tc} {count}')