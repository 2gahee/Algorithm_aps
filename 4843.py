import sys
sys.stdin=open('input4843.txt')

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    lst=list(map(int, input().split()))
    #오름차순으로 lst 정렬후 pop(0)과 pop(-1) 그리고 append이용
    for i in range(N-1):
        for j in range(N-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    stack = [] #stack리스트는 tc돌때마다 초기화

    while len(stack) < 10:  #10보다 작을때까지 돌아야 stack에는 10개 들어감
        stack.append(lst.pop(-1))
        stack.append(lst.pop(0))

    print(f'#{tc}', *stack)
