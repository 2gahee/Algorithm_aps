import sys
sys.stdin = open('Ladder1input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점 '2'를 찾는다
    for j in range(100):
        if arr[99][j] == 2:
            end_col = j
            break

    # 도착 지점에서 시작
    i, j = 99, end_col
    # 맨 밑에서 바로 한 칸 위로 이동
    i -= 1

    while i > 0:
        # 왼쪽이 1이고 범위 내에 있을 경우
        if j > 0 and arr[i][j - 1] == 1:
            while j > 0 and arr[i][j - 1] == 1:
                j -= 1
            i -= 1  #좌우 이동후 행을 꼭 이동(위로 올라가야함) (왼쪽으로 쭉 이동해왔으면, 더이상 왼쪽길이없을때 위로 올림.안그러면 다음 루프에서도 행이 그대로이므로 다시 오른쪽으로 탐방함(왔던 길 되돌아감))
        # 오른쪽이 1일 경우 오른쪽으로 이동
        elif j < 99 and arr[i][j + 1] == 1:
            while j < 99 and arr[i][j + 1] == 1:
                j += 1
            i -= 1#좌우 이동후 행을 꼭 이동(위로 올라가야함) (오른쪽으로 쭉 이동해왔으면, 더이상 오른쪽길이없을때 위로 올림.안그러면 다음 루프에서도 행이 그대로이므로 다시 왼쪽으로 탐방함(왔던 길 되돌아감))
        # 위쪽이 1일 경우 위로 이동
        elif arr[i - 1][j] == 1:
            i -= 1

    print(f'#{N} {j}')