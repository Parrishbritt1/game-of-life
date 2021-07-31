def print_board(board):
    for i in len(board):
        print(board[i])

    print()

def next_gen(board):
    for i in range(len(board)):
        for j in range(len(board)):
            alive_neighbors = get_neighbors(i, j, board)

def get_neighbors(i, j, board):
    # TOP LEFT CELL
    if i == 0 and j == 0:
        neighbors["E"] = (i, j+1)
        neighbors["SE"] = (i+1, j+1)
        neighbors["S"] = (i+1, j)
        
    # TOP RIGHT CELL
    elif i == 0 and j == len(board[i])-1:
        neighbors["W"] = (i, j-1)
        neighbors["SW"] = (i+1, j-1)
        neighbors["S"] = (i+1, j)

    # BOTTOM LEFT CELL
    elif i == len(board[i])-1 and j == 0:
        neighbors["N"] = (i-1, j)
        neighbors["NE"] = (i-1, j+1)
        neighbors["E"] = (i, j+1)

    # BOTTOM RIGHT CELL
    elif i == len(board[i])-1 and j == len(board[i])-1:
        neighbors["N"] = (i-1, j)
        neighbors["NW"] = (i-1, j-1)
        neighbors["W"] = (i, j-1)

    # TOP ROW
    elif i == 0:
        neighbors["W"] = (i, j-1)
        neighbors["SW"] = (i+1, j-1)
        neighbors["S"] = (i+1, j)
        neighbors["SE"] = (i+1, j+1)
        neighbors["E"] = (i, j+1)

    # BOTTOM ROW
    elif i == len(board[i])-1:
        neighbors["W"] = (i, j-1)
        neighbors["NW"] = (i-1, j-1)
        neighbors["N"] = (i-1, j)
        neighbors["NE"] = (i-1, j+1)
        neighbors["E"] = (i, j+1)

    # LEFT COLUMN
    elif j == 0:
        neighbors["N"] = (i-1, j)
        neighbors["NE"] = (i-1, j+1)
        neighbors["E"] = (i, j+1)
        neighbors["SE"] = (i+1, j+1)
        neighbors["S"] = (i+1, j)
        
    # RIGHT COLUMN
    elif j == len(board[i])-1:
        neighbors["N"] = (i-1, j)
        neighbors["NW"] = (i-1, j-1)
        neighbors["W"] = (i, j-1)
        neighbors["SW"] = (i+1, j-1)
        neighbors["S"] = (i+1, j)
        
    # ANY CELL NOT ON THE EDGES
    else: 
        neighbors["N"] = (i-1, j)
        neighbors["NE"] = (i-1, j+1)
        neighbors["E"] = (i, j+1)
        neighbors["SE"] = (i+1, j+1)
        neighbors["S"] = (i+1, j)
        neighbors["SW"] = (i+1, j-1)
        neighbors["W"] = (i, j-1)
        neighbors["NW"] = (i-1, j-1)

    

# board = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


board = [[0, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0]]

neighbors = {}

count = 0
alive_neighbors = 0
while count < 10:
    next_gen(board)

    count += 1