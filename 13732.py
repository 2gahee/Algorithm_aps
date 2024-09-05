import sys
sys.stdin=open('sample_input (10).txt')

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    col = 0
    count = 0
    row_count = 0
    for _ in range(N):
        lst = list(input())
        j = 0
        count = 0
        row_count=0
        flag=1
        if flag:
            while j < N and lst[j] == '#':
                if row_count > 0:
                    if j == col:
                        count += 1
                        j += 1
                        row_count += 1
                elif row_count == 0:
                    col = j
                         count += 1
                         j += 1
                         row_count += 1
                     else:
                         flag = 0
                         break
                if flag:
                    break

    if row_count == count:
      ans='yes'
    else:
        ans='no'
    print(f'#{tc} {ans}')

