import sys
sys.stdin=open('Hwemoon_input.txt')

for tc in range(1, 11):
    M = int(input())
    arr = [list(input()) for _ in range(8)]
    count =0
    #가로회문 (행부터) (회문길이 개수만큼for문 한번더 돌려야함)
    for i in range(8):
        for j in range(8-M+1):
            string = '' #초기화 문자열이므로 ''
            for k in range(0,M):
                string += arr[i][j+k] #문자열로 뽑았으므로 그냥 +
            if string == string[::-1]: #뒤집은 거랑 비교
                count += 1

    #세로회문(열부터) (회문길이 개수만큼for문 한번더 돌려야함)
    for j in range(8):
        for i in range(8-M+1):
            string = ''
            for k in range(0, M):
                string += arr[i+k][j]
            if string == string[::-1]:
                count += 1
    print(f'#{tc} {count}')