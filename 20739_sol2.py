# import sys
# sys.stdin=open('sample_in2.txt')
#
# T=int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr=[list(map(int, input().split()))for _ in range(N)]
#     # print(N,M)
#     # print(arr)
#     max_count=0
#     count=0
#     max_count_lst=[]
#
#      #  N:행  M:열
#     # 가로 탐색
#     for i in range(N):
#         for j in range(M):
#             while j<M and arr[i][j]==1:
#                 count+=1
#                 j+=1
#             if count > max_count:
#                 max_count = count
#                 max_count_lst.append(max_count)
#             count=0
#
#
#
#
#     # 세로 탐색(열탐색시 for문에 열이 먼저 와야함)
#     for i in range(M):
#         for j in range(N):
#             while i<N and arr[i][j] == 1:
#                 count += 1
#                 i += 1
#             if count > max_count:
#                 max_count = count
#                 max_count_lst.append(max_count)
#             count=0
#     max=0
#     for i in range(len(max_count_lst)):
#         if max_count_lst[i] > max:
#             max = max_count_lst[i]
#             if max==1:
#                 max=0
#
#     print(f'#{tc} {max}')

while로 푼거 틀렸음, 아직 못고침,