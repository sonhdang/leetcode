# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Pseudocode
        # First seperate moves of player A and B
        # For each player, check for the winner
        #     Checking line by line horizontally
        #     Checking line by line vertically
        #     Checking diagonally
        # Finally check whether the number of moves are equal to the number of squares
        #     if yes -> draw
        #     if no -> pending
        a_moves = moves[0::2]
        b_moves = moves[1::2]
        grid = [["." for _ in range(3)] for _ in range(3)]
        for i,j in a_moves:
            grid[i][j] = "A"
        
        for i,j in b_moves:
            grid[i][j] = "B"
            
        
        # Checking horizontally
        for row in grid:
            if row[0] == 'A' or row[0] == 'B':
                winner = row[0]
                if winner == row[1] and winner == row[2]:
                    return winner
                else:
                    continue
        
        # Checking vertically
        for j in range(3):
            for i in range(3):
                if grid[i][j] == 'A' or grid[i][j] == 'B':
                    winner = grid[i][j]
                    if winner == grid[i+1][j] and winner == grid[i+2][j]:
                        return winner
                    else:
                        break
                else:
                    break
        
        # Check Diagonal
        winner = grid[1][1]
        if winner != '.' and ((winner == grid[0][0] and winner == grid[2][2]) or (winner == grid[2][0] and winner == grid[0][2])):
                return winner
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"