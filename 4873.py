import sys
sys.stdin= open('input4873.txt')

T=int(input())
for tc in range(1,T+1):
    str_lst = list(map(str, input()))
    # print(str_lst)
    stack=[]
    for i in range(len(str_lst)):
        if len(stack) == 0:
            stack.append(str_lst[i])
        elif stack[-1] == str_lst[i]:
            stack.pop()
        elif stack[-1] != str_lst[i]:
            stack.append(str_lst[i])

    print(f'#{tc}', len(stack))