from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# This is a depth-first search algorithm for solving Sudoku.
# It starts from the top left cell, fills it with a number from 1 to 9
# and then moves to the next cell (left to right, top to bottom).
# If a valid number can't be found for a cell, it "backtracks" to previous cells
# and tries the next possible number.
def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

# This function checks if it's valid to put a number in a specific cell.
# It checks the current row, column, and 3x3 box.
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# This function finds an empty cell in the board (left to right, top to bottom).
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

# This is the main route of our Flask API.
# It receives a POST request containing the Sudoku board to be solved,
# solves the Sudoku and returns the solved board.
@app.route('/', methods=['POST'])
def solve():
    data = request.get_json()

    board = data['board']
    
    if solve_sudoku(board):
        return jsonify({'status': 'solved', 'board': board})
    else:
        return jsonify({'status': 'no solution', 'board': board})

if __name__ == "__main__":
    app.run(port=3002, debug=True)
