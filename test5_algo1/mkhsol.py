T = int(input())            # 전체 테스트 케이스
for tc in range(1, T+1):
    N = int(input())        # 배열의 길이
    arr = input()           # 배열, str의 형태로 받아온다.
    m_cnt = 1               # 최대값을 비교해서 저장해둘 변수 m_cnt. 최솟값은 1
    for i in range(1, N):   # 0번은 대칭일 수 없으므로 1번부터
        cnt = 1             # 해당 번호의 대칭을 카운트하는 변수 cnt
        for j in range(1, N):       # 적당히 큰 수 동안 양 옆을 세는데
            if i+j < N and i-j >= 0 and arr[i-j]==arr[i+j]:     # i+j나 i-j가 범위를 벗어나지 않고 양 옆의 값이 같다면
                cnt += 2    # cnt에 2를 더해준다.
            else: break     # 만약 같지 않을 경우 추가로 볼 이유가 없으므로 반복문을 나간다.
        if m_cnt < cnt: m_cnt = cnt     # 매 요소를 확인한 후 m_cnt를 확인하여 갱신시켜준다.
    print(f'#{tc} {m_cnt}')