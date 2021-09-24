def get_neighbors(i, j, board, alive_neighbors):
    """Returns a dictionary containing current cell as key and their respective amount neighboring alive cells
    
    Keyword arguments:
    i -- row index
    j -- column index
    alive_neighbors - dictionary that will be returned at the end (this dictionary is reset in next_gen function)
    """
    neighbors_pos = {}

    # TOP LEFT CELL
    if i == 0 and j == 0:
        neighbors_pos["E"] = (i, j+1)
        neighbors_pos["SE"] = (i+1, j+1)
        neighbors_pos["S"] = (i+1, j)
        
    # TOP RIGHT CELL
    elif i == 0 and j == len(board[i])-1:
        neighbors_pos["W"] = (i, j-1)
        neighbors_pos["SW"] = (i+1, j-1)
        neighbors_pos["S"] = (i+1, j)

    # BOTTOM LEFT CELL
    elif i == len(board)-1 and j == 0:
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NE"] = (i-1, j+1)
        neighbors_pos["E"] = (i, j+1)

    # BOTTOM RIGHT CELL
    elif i == len(board)-1 and j == len(board[i])-1:
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NW"] = (i-1, j-1)
        neighbors_pos["W"] = (i, j-1)

    # TOP ROW
    elif i == 0:
        neighbors_pos["W"] = (i, j-1)
        neighbors_pos["SW"] = (i+1, j-1)
        neighbors_pos["S"] = (i+1, j)
        neighbors_pos["SE"] = (i+1, j+1)
        neighbors_pos["E"] = (i, j+1)

    # BOTTOM ROW
    elif i == len(board)-1:
        neighbors_pos["W"] = (i, j-1)
        neighbors_pos["NW"] = (i-1, j-1)
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NE"] = (i-1, j+1)
        neighbors_pos["E"] = (i, j+1)

    # LEFT COLUMN
    elif j == 0:
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NE"] = (i-1, j+1)
        neighbors_pos["E"] = (i, j+1)
        neighbors_pos["SE"] = (i+1, j+1)
        neighbors_pos["S"] = (i+1, j)
        
    # RIGHT COLUMN
    elif j == len(board[i])-1:
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NW"] = (i-1, j-1)
        neighbors_pos["W"] = (i, j-1)
        neighbors_pos["SW"] = (i+1, j-1)
        neighbors_pos["S"] = (i+1, j)
        
    # ANY CELL NOT ON THE EDGES
    else: 
        neighbors_pos["N"] = (i-1, j)
        neighbors_pos["NE"] = (i-1, j+1)
        neighbors_pos["E"] = (i, j+1)
        neighbors_pos["SE"] = (i+1, j+1)
        neighbors_pos["S"] = (i+1, j)
        neighbors_pos["SW"] = (i+1, j-1)
        neighbors_pos["W"] = (i, j-1)
        neighbors_pos["NW"] = (i-1, j-1)

    # Loop through each possible neighbor
    for neighbor_dir in neighbors_pos:
        # Get neighbor position ex: (i+1, j) one row down and same column
        pos = neighbors_pos[neighbor_dir]
        # If that neighbor is alive
        if board[pos[0]][pos[1]] == 1:

            # check if current cell is in alive_neighbors and add one alive neighbor 
            if (i, j) in alive_neighbors:
                alive_neighbors[(i, j)] += 1
            else:
                alive_neighbors.setdefault((i, j), 1)
    
    return alive_neighbors


def next_gen(board):
    """Returns a 2d array of the next generation of board"""
    alive_neighbors = {}
    # Loop through the board and create alive_neighbors 
    # which contains Key: current cell - Value: # of alive neighbors 
    for i in range(len(board)):
        for j in range(len(board[i])):
            alive_neighbors = get_neighbors(i, j, board, alive_neighbors)

    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[i])):
            # Cell has alive neighbors
            if (i, j) in alive_neighbors:

                # Current cell is alive
                if board[i][j] == 1:
                    # Cell has less than 2 neighbors (UNDERPOPULATION)
                    if alive_neighbors[(i, j)] < 2:
                        new_board[i].append(0) 
                    # Cell has 2 or 3 neighbors (LIVES ON)
                    elif alive_neighbors[(i, j)] == 2 or alive_neighbors[(i, j)] == 3:
                        new_board[i].append(1)
                    # Cell has more than 3 neighbors (OVERPOPULATION)
                    else:
                        new_board[i].append(0)

                # Current cell is dead
                else:
                    # Cell has 3 neighbors (REPRODUCTION)
                    if alive_neighbors[(i, j)] == 3:
                        new_board[i].append(1)
                    else:
                        new_board[i].append(0)
                  
            # Cell has no alive neighbors 
            else:
                new_board[i].append(0)  

    return new_board
    

def main():
    board = [[0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

    count = 0
    while count < 10:
        print(board)
        board = next_gen(board)
        count += 1


if __name__ == "__main__":
    main()