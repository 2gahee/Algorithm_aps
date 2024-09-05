import sys
sys.stdin =open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    sort_list = sorted(lst)
    ans = 0
    while dump > 0:
        a = sort_list.pop()
        sort_list.append(a-1)
        b = sort_list.pop(0)
        sort_list.append(b+1)
        sort_list = sorted(sort_list)
        dump -= 1
        if sort_list[0] == sort_list[-1]:
            break
    ans = sort_list[-1] - sort_list[0]

    print(f'#{tc} {ans}')


sort

