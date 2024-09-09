# 1
# 5
# 14054
# 44250
# 02032
# 51204
# 52212

#농작물 수확
# 1번 풀이: start, end로 풀기
# 2번 풀이: 행과 열 사이에서 규칙찾아 일반화하기



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    S = N//2
    E = N//2
    total = 0
    1번 풀이
    for i in range(N):
        for j in range(S, E+1):
            total += arr[i][j]
        if i < N//2:
            S -= 1
            E += 1
        else:
            S += 1
            E -= 1

    print(f'#{tc} {total}')


    # 2번 풀이
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i, N-(N//2-i)):
                total += arr[i][j]
        if  i > N//2:
            for j in range(i-N//2, N-(i-N//2)):
                total += arr[i][j]
    print(f'#{tc} {total}')

