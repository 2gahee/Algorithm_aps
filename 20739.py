import sys
sys.stdin=open('sample_in2.txt')

T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr=[list(map(int, input().split()))for _ in range(N)]
    # print(N,M)
    # print(arr)
    max_count=0

    # 가로 탐색
    for i in range(N):
        count=0
        for j in range(M):
            if arr[i][j] == 1:
               count+=1
               if count > max_count:
                  max_count = count
            else:
                count=0

    # 세로 탐색(열탐색시 for문에 열이 먼저 와야함)
    for i in range(M):
        count=0
        for j in range(N):
            if arr[j][i]==1:
                count+=1
                if count > max_count:
                    max_count = count
            else:
                count = 0

    if max_count==1:
        max_count=0

    print(f'#{tc} {max_count}')