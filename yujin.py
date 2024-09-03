board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
basket=[]
count=0
for i in range(len(moves)):
    for j in range(len(board)):
        if board[j][moves[i]-1] != 0: #인형이 있다면
            basket.append(board[j][moves[i]-1]) #인형 basket에 추가하고
            board[j][moves[i] - 1]=0  #인형을 가져갔으므로 0으로 바꿔놓음

            if len(basket) > 1: #basket에 인형이 2개이상일때
                if basket[-2] == basket[-1]:
                    basket.pop()
                    basket.pop()
                    count+=2
            else:
                break

print(count)


# def solution(board, moves):
#     stacklist = []
#     answer = 0
#
#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0
#
#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop(-1)
#                         stacklist.pop(-1)
#                         answer += 2
#                 break
#
#     return answer