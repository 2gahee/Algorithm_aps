import sys
sys.stdin=open('sample_input (2).txt')

#상자 한개씩 색칠하는 개념으로 풀기
#주어진 정보에서 같은 색인 영역은 겹치지 않는다는게 중요

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr=[[0]*10 for _ in range(10)]  #해당하는 상자들을 색칠하기위해 전체배열을 일단 0으로 만들어놓음
    count=0 #겹쳐지는 부분 count

    for _ in range(N):  #상자개수만큼 순회
        r1, c1, r2, c2, color = map(int, input().split()) #각각 불러옴(상자 하나씩 색칠)
        # print(r1, c1, r2, c2, color)
        for i in range(r1, r2+1):   # 상자의 가로만큼 순회
            for j in range(c1, c2+1): #상자의 세로만큼 순회
                arr[i][j] += color   #상자에 해당하는 색깔 칠해줌
                if arr[i][j]==3:   #상자에 (빨1+파2==3) 겹쳐진 부분있으면 개수 세기
                    count+=1
    print(f'#{tc} {count}')


