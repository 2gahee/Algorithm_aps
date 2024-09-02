def inorder(arr, n):        # 중위 순회로 탐색할 arr와 1로 시작하는 인덱스 번호
    if n <4:                # 자식이 있는 노드라면
        inorder(arr,n*2)    # 중위 순회 왼쪽 자식
        print(arr[n], end='')
        inorder(arr,n*2+1)  # 중위 순회 오른쪽 자식
    else: print(arr[n], end='')
# 문제의 조건상 들어오는 배열이 항상 높이가 3인 완전 이진트리이므로 위와 같이 작성해도 괜찮다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # arr의 길이를 나타내는 N
    arr = input()       # 전체 문자열 arr
    bin = [0] * N       # 각 문자열의 아스키 코드를 2진수로 담을 빈 리스트 bin

    for i in range(N):
        num = ord(arr[i])   # arr의 글자를 아스키코드로 변환한 후
        b = ''              # 이진수를 담을 빈 str 선언
        for _ in range(7):  # 7자리 이진수로 변환하여 b에 담아준다.
            if num % 2:
                b = '1' + b
            else: b = '0' + b
            num //= 2
        bin[i] = ' ' + b          # bin에다가 이진수로 변환된 값을 쌓아준다. 문자열 인덱스 접근을 쉽게 하기 위해 공백 추가.

    print(f'#{tc} ', end= '')        # 정답 출력
    for i in range(N):
        inorder(bin[i],1)   # 글자마다 중위순회
        print(' ', end='')  # 글자간 공백
    print()                 # 줄바꿈