board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
         
moves = [1,5,3,5,1,2,1,4]

    
def solution(board,moves):
    result = 0
    box = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            
            else:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
    
        if len(box)>=2 and  box[-1] == box[-2] :
            box.pop(-1)
            box.pop(-1)
            result+=1
    
    return result*2

print(solution(board,moves))