import sys
sys.stdin=open('input1974.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    lst = [0, 3, 6]

    # 3*3격자 확인 (파리채마냥 돌기)
    for k in lst:   # 파리채의 시작점
        Nemo = []   # 시작점 바뀔때 마다 초기화
        if ans:    # flag로 ans=0이면 아래 반복문 실행 X
            for i in range(3):
                if ans:  # flag로 ans=0이면 아래 반복문 실행 X
                    for j in range(3):
                        if arr[k+i][k+j] in Nemo:
                            ans=0
                            break   #가장 가까운 for문 탈출

                        else:
                            Nemo.append(arr[k+i][k+j])
                else:
                    break  # flag로 ans=0이면 break로 해당 for문 빠져나옴
        else:
            break   # flag로 ans=0이면 break로 해당 for문 빠져나옴


    # 가로 탐색 (행부터)
    if ans:   # flag로 ans=0이면 아래 반복문 실행 X
        for i in range(9):
            Nemo = []
            if ans:
                for j in range(9):
                    if arr[i][j] in Nemo:
                        ans = 0
                        break
                    else:
                        Nemo.append(arr[i][j])
            else:
                break
    # 세로 탐색    (열부터)
    if ans:  # flag로 ans=0이면 아래 반복문 실행 X
        for j in range(9):
            Nemo = []
            if ans: # flag로 ans=0이면 아래 반복문 실행 X
                for i in range(9):
                    if arr[i][j] in Nemo:
                        ans = 0
                        break
                    else:
                        Nemo.append(arr[i][j])
            else:
                break

    print(f'#{tc} {ans}')





