class Solution:
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        step = 0
        path = 0
        for i in range(n):
            box = []
            D1=set()
            D2=set()
            D3=set()
            if step==9:
                step=0
                path+=3
            box+=board[path][step:step+3]+board[path + 1][step:step+3]+board[path+2][step:step+3]
            print(box)
            step+=3
            for j in range(n):
                
                if box[j] in D3:
                    return False
                elif box[j]!=".":
                    D3.add(box[j])

                if board[i][j] in D1  :
                    return False
                elif board[i][j]!=".":
                    D1.add(board[i][j])
                if board[j][i] in D2 :
                    return False
                elif board[j][i]!=".":
                    D2.add(board[j][i])
                print(board[i][j],board[j][i],box[j])

        return True