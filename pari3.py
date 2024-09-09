import sys
sys.stdin=open('in1.txt')
# 파리퇴치3  12712
T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #대각선의 델타
    dx1 = [-1, -1, +1, +1]
    dy1 = [-1, +1, -1, +1]
    #십자가의 델타
    dx2 = [-1, 0, +1, 0]
    dy2 = [0, +1, 0, -1]
    max_sum = 0
    for i in range(N): #전체 배열 순회
        for j in range(N):
            sum = 0
            # cross_sum = arr[i][j]  # cross_sum의 기준값 정해줌(본인)(가운뎃값)   x
            # plus_sum = arr[i][j]   # plus_sum의 기준값 정해줌(본인)(가운뎃값)    +
            for k in range(4): # 델타값 순회
                for m in range(0, M): # 기준칸으로부터 몇칸 갈 수 있는 지 = M값 순회
                    nx1 = i + dx1[k] * m
                    ny1 = j + dy1[k] * m
                    if 0 <= i + dx1[k] * m < N and 0 <= j + dy1[k] * m < N:  # 배열에서 벗어나지 않는 범위만 더해줌
                        sum += arr[nx1][ny1]
                        if sum > max_sum:
                            max_sum = sum


    for i in range(N):  # 전체 배열 순회
        for j in range(N):
            sum = 0
            # cross_sum = arr[i][j]  # cross_sum의 기준값 정해줌(본인)(가운뎃값)   x
            # plus_sum = arr[i][j]   # plus_sum의 기준값 정해줌(본인)(가운뎃값)    +
            for k in range(4):  # 델타값 순회
                for m in range(0, M):  # 기준칸으로부터 몇칸 갈 수 있는 지 = M값 순회
                    nx2 = i + dx2[k] * m
                    ny2 = j + dy2[k] * m
                    if 0 <= i + dx2[k] * m < N and 0 <= j + dy2[k] * m < N:  # 배열에서 벗어나지 않는 범위만 더해줌
                        sum += arr[nx2][ny2]
                        if sum > max_sum:
                            max_sum = sum

    print(f'#{tc} {max_sum}')