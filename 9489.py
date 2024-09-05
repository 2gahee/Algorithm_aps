import sys
sys.stdin=open('input1.txt')
T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    #가로 탐색
    for i in range(N): #행
        count = 0      #행 바뀔때마다 초기화
        for j in range(M): #열
            if arr[i][j] == 1:
                count += 1
                if count > max_count:    #count최대값구하기
                    max_count = count
            else:              #1이 아니면 count초기화
                count = 0
    #세로 탐색
    for i in range(M):   #열
        count = 0        #열 바뀔때마다 초기화
        for j in range(N): #행
            if arr[j][i] == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

    print(f'#{tc} {max_count}')