import sys
sys.stdin=open('sample_input (1).txt')

T=int(input())
for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    chargestation=list(map(int, input().split()))
    # print(K, N, M)
    # print(chargestation)
    start=0
    i=0
    res=0
    count=0
    count=0



    while i < M  and start+K < N:  #i가 충전소정류장개수보다 작고, N에 도착하기 전 까지 반복
        if chargestation[i] - start < K:  # 충전정류장-현재위치가 K보다 작을때 다음 충전정류장 - 현재위치를 본다.
            i+=1
            if chargestation[i] - start == K:  # 다음충전정류장-현재위치가 k면 거기서 충전횟수+1 현재위치를 해당정류장으로 갱신
                count+=1
                start=chargestation[i]
                i+=1
            elif chargestation[i] - start > K: # 다음충전정류장-현재위치가 k보다 크면 이전 충전정류장으로 돌아가서 충전횟수+1 현재위치를 해당 정류장으로 갱신
                i-=1
                count+=1
                start=chargestation[i]
                i+=1


        elif chargestation[i] - start > K: #충전정류장-현재위치>K면 더이상 진행불가 그냥 반복문탈출,, 0으로 출력
            count=0
            break



    # for j in range(len(count)):
    #     res+=count[j]

    print(f'#{tc} {count}')

            
