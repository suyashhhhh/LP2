def isSafe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solveNQueen(board, row, N, count):
    if row == N:
        # All queens have been placed, solution found
        count[0] += 1
        print("Solution", count[0], ":")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
        print()
        return

    for col in range(N):
        if isSafe(board, row, col, N):
            # Place queen at board[row][col]
            board[row][col] = 1

            # Check if placing this queen leads to a valid solution
            if isValidPartialSolution(board, row, col, N):
                # Recursively solve for next row
                solveNQueen(board, row + 1, N, count)

            # Backtrack and remove the queen
            board[row][col] = 0


def isValidPartialSolution(board, row, col, N):
    # Check if there is a queen in the same column or in the diagonal of the current position
    for i in range(row + 1, N):
        if board[i][col] == 1:
            return False

        j = col - (i - row)
        if j >= 0 and board[i][j] == 1:
            return False

        j = col + (i - row)
        if j < N and board[i][j] == 1:
            return False

    return True


def main():
    N = int(input("Enter the number of queens: "))
    board = [[0] * N for _ in range(N)]
    count = [0]

    solveNQueen(board, 0, N, count)

    print("Total solutions:", count[0])


main()
