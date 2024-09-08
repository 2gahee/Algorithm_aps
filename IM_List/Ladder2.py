import sys
sys.stdin=open('Ladder2_input.txt')

#도착지가 1인 것(99행이 1인것들 모두 탐색 갈때마다 1씩 더함  그래서 그 count가 가장 적은 0번째 행의 열 구하기)
#사다리타기는 밑에서 위로 이동하므로
#왼쪽과 오른쪽이 무조건 우선시 그리고 위로 올라가는 순서
#왼쪽길 있을경우 왼쪽 끝까지 이동while문 사용( 단, 끝까지 갔을 떄 다시 왔던 길로 안가려면 즉, 오른쪽으로 안가려면 행 올려주기)
#오른쪽길 있을 경우 오른쪽 길 끝까지 이동while문 사용( 단, 끝까지 갔을 떄 다시 왔던 길로 안가려면 즉, 왼쪽으로 안가려면 행 올려주기)
#오른쪽 왼쪽 길 없고 위만 있으면 위로 행하나 이동(단, 오른쪽 왼쪽이 나타나면 언제든 오른쪽 왼쪽 으로 가야하기에 while문 안씀)
#끝점 찾은뒤 99행이 아닌 98행에서 시작(마지막은 위로 밖에 없음)

for tc in range(1,11):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(100)]
    min_count = 10000
    ans = 0
    for j in range(100):
        if arr[99][j]==1:
            sj = j
            si = 98
            count=0
            while si != 0:
                #오른쪽에 1있을떄
                if sj < 99 and arr[si][sj+1]==1:  #꼭 인덱스 범위가 앞에 먼저 와야해
                    while sj < 99 and arr[si][sj+1]==1:
                        sj += 1
                        count += 1
                    si -= 1   #왔던 길 다시 왼쪽으로 가지 않기 위해 행 올려줘야함
                #왼쪽에 1있을떄
                elif sj > 0 and arr[si][sj-1]==1:
                    while sj > 0 and arr[si][sj-1]==1:
                        sj -= 1
                        count += 1
                    si -= 1
                #위쪽에만 1있을때
                elif si > 0 and arr[si - 1][sj] == 1:
                    si -= 1
                    count += 1

            if min_count >= count:  #  if arr[99][j]==1:일때마다 최솟값 갱신
                min_count = count
                ans = sj  #min count에 해당하는 열 출력

    print(f'#{tc} {ans}')