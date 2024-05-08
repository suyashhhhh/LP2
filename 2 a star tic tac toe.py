def evaluate(board):
    lines = [
        [(0, 0), (1, 0), (2, 0)],  # Rows
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],  # Columns
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # Diagonals
        [(2, 0), (1, 1), (0, 2)]
    ]

    for line in lines:
        markers = []
        for x, y in line:
            markers.append(board[x][y])
        if markers == ['X', 'X', 'X']:
            return 1
        elif markers == ['O', 'O', 'O']:
            return -1

    return 0

def get_possible_moves(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                possible_moves.append((i, j))
    return possible_moves

def make_move(board, move, player):
    board[move[0]][move[1]] = player

def undo_move(board, move):
    board[move[0]][move[1]] = ' '

def is_game_over(board):
    win_conditions = [
        board[0][0] == board[0][1] == board[0][2] != ' ',  # Rows
        board[1][0] == board[1][1] == board[1][2] != ' ',
        board[2][0] == board[2][1] == board[2][2] != ' ',
        board[0][0] == board[1][0] == board[2][0] != ' ',  # Columns
        board[0][1] == board[1][1] == board[2][1] != ' ',
        board[0][2] == board[1][2] == board[2][2] != ' ',
        board[0][0] == board[1][1] == board[2][2] != ' ',  # Diagonals
        board[2][0] == board[1][1] == board[0][2] != ' '
    ]

    if any(win_conditions) or all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True
    else:
        return False

def astar(board, depth, maximizing_player):
    if is_game_over(board):
        return evaluate(board)

    if maximizing_player:
        best_score = float('-inf')
        possible_moves = get_possible_moves(board)
        for move in possible_moves:
            make_move(board, move, 'X')
            score = astar(board, depth + 1, False)
            undo_move(board, move)
            if score > best_score:
                best_score = score
        return best_score
    else:
        best_score = float('inf')
        possible_moves = get_possible_moves(board)
        for move in possible_moves:
            make_move(board, move, 'O')
            score = astar(board, depth + 1, True)
            undo_move(board, move)
            if score < best_score:
                best_score = score
        return best_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    possible_moves = get_possible_moves(board)
    for move in possible_moves:
        make_move(board, move, 'X')
        score = astar(board, 0, False)
        undo_move(board, move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while not is_game_over(board):
        print(f"\nPlayer {current_player}'s turn")
        if current_player == 'X':
            move = get_best_move(board)
        else:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            move = (row, col)

        if move not in get_possible_moves(board):
            print("Invalid move. Try again.")
            continue

        make_move(board, move, current_player)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        print_board(board)

    winner = evaluate(board)
    if winner == 1:
        print("\nPlayer X wins!")
    elif winner == -1:
        print("\nPlayer O wins!")
    else:
        print("\nIt's a draw!")

play_tic_tac_toe()
