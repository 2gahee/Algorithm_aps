#돌뒤집기게임2    #20397

import sys
sys.stdin=open('sample_in.txt')

T=int(input())
for tc in range(1,T+1):
    N, M= map(int, input().split())  # N개 돌, M번 뒤집기
    original_lst=list(map(int,input().split()))  # 초기 돌의 상태를 리스트로 받아옴
    for _ in range(M):  # M번 순회하며 M번의 i,j를 받아옴
        i, j = map(int, input().split()) #i,j 받아옴
        # print(original_lst)
        # print(i,j)
        for idx in range(1, j + 1):   #i의 옆 칸인 j를 순회
            if i-1+idx <= N-1 and i-1-idx >= 0: #i는 첫번째부터 시작 즉, 1이 0번째인덱스임.그러므로 i-1해줌,그리고 옆칸의 범위가 0과 N사이야함
                  if original_lst[i-1+idx] == original_lst[i-1-idx] == 1: #둘 다 1이면 0으로 바꿔줌
                     original_lst[i-1 + idx]=0
                     original_lst[i-1 - idx]=0

                  elif original_lst[i-1+idx] == original_lst[i-1-idx] == 0:#둘 다 0이면 1로 바꿔줌
                       original_lst[i-1 + idx]=1
                       original_lst[i-1 - idx] = 1

    print(f'#{tc}', *original_lst)   # *사용해 unpacking한 값 출력

