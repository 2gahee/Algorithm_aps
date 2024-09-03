board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
basket=[0]
count=0

for i in range(len(moves)):
    for j in range(len(board)):
        if board[j][moves[i]-1]!= 0:
            if board.pop() == basket[-1]:
                basket.pop()
                count+=2
            if board.pop() != basket[-1]:
                basket.append(board.pop())



print(count)
