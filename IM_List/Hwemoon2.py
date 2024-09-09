import sys
sys.stdin = open('hwemoon2_input.txt')

#가로 탐색 세로 탐색 모두 해서 길이가 가장 긴 회문 찾기
#A도 길이1인 회문

for tc in range(1,11):
    T=int(input())
    arr = [list(input()) for _ in range(100)]
    max_len = 0

    #가로탐색
    for i in range(100):
        # str = ''
        for j in range(100):
                k =0
                str = ''
                for k in range(100):
                    if j+k <= 99:
                        str += arr[i][j + k]
                        # k += 1
                        if str == str[::-1]:
                            if max_len < len(str):
                                max_len = len(str)
    #세로 탐색
    for j in range(100):
        # str = ''
        for i in range(100):
            k=0
            str = ''
            for k in range(100):
                if i+k <= 99:
                    str += arr[i+k][j]
                    # k += 1
                    if str == str[::-1]:
                        if max_len < len(str):
                            max_len = len(str)

    print(f'#{tc} {max_len}')



