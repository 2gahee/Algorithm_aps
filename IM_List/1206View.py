import sys
sys.stdin=open('sample_input (6).txt')

for tc in range(1,11):
    N = int(input())
    lst = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        lst2 = []
        if lst[i] > lst[i-2] and  lst[i] > lst[i-1] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            lst2.append(lst[i+1])
            lst2.append(lst[i+2])
            lst2.append(lst[i-1])
            lst2.append(lst[i-2])
            second_max = max(lst2)
            total += lst[i] - second_max
    print(f'#{tc} {total}')

    
    # max