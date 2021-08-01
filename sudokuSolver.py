# main function
def main():
    file = open("input.txt", 'r')
    board = loadBoard(file)
    print("Input:")
    printBoard(board)
    solve(board)
    print("Done!!!" + "\n" + "Check file for output")
    writeToFile(board)


# read a text file
def loadBoard(file):
    with open("input.txt") as file:
        board = []
        for line in file:
            # adds every element to a list board
            board.append([elem for elem in line.split(',')])
    return board


# write the output to file
def writeToFile(board):
    with open("output.txt", 'w') as file:
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                file.write("- - - - - - - - - - - - " + "\n")

            for j in range(len(board[0]) - 1):
                if j % 3 == 0 and j != 0:
                    file.write(" | ")

                if j == 8:
                    file.write(str(board[i][j]) + " " + "\n")
                else:
                    file.write(str(board[i][j]) + " ")


# print a board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0]) - 1):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j] + " ", end="")


# return the index of the empty square on board
def findEmptySquare(board):
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            if board[i][j] == '*':
                return i, j
    return False


def checkValidity(board, value, position):
    # check if it is possible to place a number in a row
    for j in range(len(board[0]) - 1):
        if board[position[0]][j] == value and position[1] != j:
            return False

    # check if it is possible to place a number in a column
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] != i:
            return False

    # check the square
    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    return True


# solver function
def solve(board):
    find = findEmptySquare(board)
    # base case if the board is full -> found a solution
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        # if the value is appropriate to be inserted -> insert it in the board
        if checkValidity(board, str(i), (row, col)):
            board[row][col] = str(i)

            if solve(board):
                return True
            # backtrack
            board[row][col] = '*'

    return False


main()
