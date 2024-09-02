# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    # print(lst)
    count = 1
    count_lst=[0]*N
    for i in range(1,len(lst)-1):  #기준이 되는 수 (기준이 되는 수를 순회)
        count = 1   #기준이 되는 수가 바뀔때마다 count초기화
        if i >= N / 2:    #기준이 되는 수가 lst길이보다 클 때
            k=1
            while k < len(lst)-i and lst[i + k] == lst[i - k]:     #리스트인덱스범위맞혀 양쪽값이 같을때까지 순회 같으면 +2씩
                  count += 2
                  # if lst[i + k] != lst[i - k]:   #다르면 while문 탈출
                  #    break
                  k += 1
                  count_lst[i]=count    #count를 count리스트에 넣음

        elif i < N / 2: #기준이 되는 수가 lst길이보다 작을 때
            h=1
            while h <= i and lst[i + h] == lst[i - h]:   #위와 동일한 방식으로 count를 구한뒤count리스트에 삽입
                  count += 2
                  # if lst[i + h] != lst[i - h]:
                  #     count_lst[i] = count
                  #     break
                  h+= 1
                  count_lst[i]=count



    maxi=1
    for idx in range(len(count_lst)):  #count리스트에서 제일 큰 값 찾아서 출력
        if count_lst[idx] > maxi:
            maxi= count_lst[idx]


    print(f'#{tc} {maxi}')