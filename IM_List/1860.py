import sys
sys.stdin =open('input1860.txt')

#thinking
# 무조건 손님 1명한테는 1개의 붕어빵을 판매하기 때문에 하나씩 카운트를 해주면 된다.
#
# 0초부터 M초 마다 붕어를 만듦으로 M, 2M, 3M, ... 초 마다 K, 2K, 3K의 붕어빵이 남는다.
#
# 그렇다면 일반적으로 x초 일때의 붕어 생산량과 그 전에 사간 사람의 수를 빼면 x초의 붕어빵 재고를 알 수 있다.
#
# 재고가 음수가 되면 다 팔렸다는 뜻이므로 Impossible 을 출력하면 된다.
#
# 손님이 온 시간을 arrive_time 이라는 리스트에 담아 올림차순으로 소팅을 해준 후,
#
# 소팅한 arrive_time 리스트를 순회하며 가장 적은 시간부터 순서대로 체킹을 했다.
#
# 일반적으로 x초까지 만들어진 붕어 개수는 (x // M) * K 이다.
#
# 왜냐하면 단위 시간(M)으로 나눈 몫만큼 만들 수 있고, 그때마다 K개를 만들기 때문이다.
#
# 인당 1개씩 구매하기 때문에 (x // M) * K 에서 인덱스+1 만큼 빼주면 된다.




T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 'Possible'
    for i in range(N):
        food = (lst[i] // M) * K
        if food < i+1:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')
