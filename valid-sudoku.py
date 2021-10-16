class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    # General Idea
    # - Check row from top to bottom
    # - check column from left to right
    # - check 3x3
    
    # Pseudocode
    # 1 dictionary for checking row by row
    # 9 dictionary for 9 colums
    # 3 dictionary for check 3 square 3x3
    
        i = 0
        
        columns = [set() for _ in range(9)]
        row = set()
        while i < 9:
            squares = [set() for _ in range (3)]
            for _ in range(3):
                j = 0   # column index
                k = 0   # square index
                while k < 3:
                    for _ in range(3):
                        if board[i][j] != '.':
                            # check row
                            if board[i][j] in row:
                                return False
                            else:
                                row.add(board[i][j])

                            # check column
                            if board[i][j] in columns[j]:
                                return False
                            else:
                                columns[j].add(board[i][j])

                            # check square
                            if board[i][j] in squares[k]:
                                return False
                            else:
                                squares[k].add(board[i][j])

                        j += 1  # move to the right by one unit
                    k += 1  # move to the right by one square
                i+= 1   # move down by one unit
                row.clear() # clear row
            
        return True
        