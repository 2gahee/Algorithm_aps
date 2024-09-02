# import sys
# sys.stdin=open('input (9).txt')
#
# T=int(input())
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     A_lst=list(map(int, input().split()))
#     B_lst = list(map(int, input().split()))
#
#     if N > M:
#         min=len(B_lst)
#         max=len(A_lst)
#         max_lst=A_lst
#         min_lst=B_lst
#     else:
#         min= len(A_lst)
#         max = len(B_lst)
#         max_lst=B_lst
#         min_lst = A_lst
#
#     max_total=float('-inf')
#     for i in range(0, max-min+1):
#         total=0
#         for k in range(0,M):
#             multi = max_lst[i+k]*min_lst[k]
#             total+=multi
#             if total > max_total:
#                 max_total=total
#
#     print(f'#{tc} {max_total}')
#

