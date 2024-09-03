import sys
sys.stdin=open('input.txt')


# T=int(input())
# for tc in range(1,T+1):
#     N, M= map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(N)]
#     # print(N,M)
#     # print(arr)
#     max_total=0
#     for k in range(0,N-M+1):  # k,l은 M*M파리채의 기준이 갈 수 있는 범위 순회 ( 즉 파리채의 왼쪽 상단이 기준)
#         for l in range(0,N-M+1):
#             total = 0          # 파리채의 기준이 바뀔때마다 0으로 초기화
#             for h in range(0, M): #파리채 기준에서 파리채 크기만큼 행에 범위 더하기
#                 for o in range(0, M): #파리채 기준에서 파리채 크기만큼 열에 범위 더하기
#                     total += arr[k+h][l+o] # 합산
#                     if total > max_total: # 합산 값 중 최댓값 찾기
#                         max_total = total
#     print(f'#{tc} {max_total}')






T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_arr = [list(map(int, input().split())) for _ in range(N)]  # 전체 배열 리스트

    max_sum = float('-inf')

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            M_sum = 0
            for k in range(M):
                for h in range(M):
                    M_sum += N_arr[i + k][j + h]  # M_arr이 아닌 N_arr의 값을 써야함

                    if M_sum > max_sum:
                        max_sum = M_sum

    print(f'#{tc} {max_sum}')

