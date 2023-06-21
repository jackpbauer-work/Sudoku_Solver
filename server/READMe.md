# Sudoku Solver

Sudoku Solver is a web application that solves Sudoku puzzles. The frontend is built with React and the backend is a Flask API. The Sudoku solving algorithm is implemented in Python.

## Installation

Clone the repository:
git clone https://github.com/<your-github-username>/sudoku-solver.git

Install the required Python packages:
cd sudoku-solver
pip install flask flask-cors

Install the required Node.js packages:
cd client
npm install

## Usage
Start the Flask API server:
python app.py
The API will start running on http://localhost:3002/.

In a new terminal window, navigate to the client directory and start the React app:
cd client
npm start
The app will start running on http://localhost:3000/.

Open http://localhost:3000/ in your web browser. You should see the Sudoku solver interface. Fill in the Sudoku board and click the "Solve" button to solve the Sudoku.

Flask web server that exposes a single endpoint (`/`) that accepts POST requests. It takes a JSON object as input with a key `board` that represents a Sudoku board as a 9x9 matrix. It attempts to solve the Sudoku board using a backtracking algorithm and then returns the solved board if a solution exists. If a solution does not exist, it returns the same input board.

The main parts of this algorithm are:

1. `solve_sudoku(board)`: This function is the main part of the backtracking algorithm. It finds an empty cell in the Sudoku board, tries to fill it with a number (from 1 to 9), and then calls itself recursively to solve the rest of the board. If it can't find a valid number for a cell, it "backtracks" by setting the cell back to empty (0) and then returning False, which makes the algorithm try the next number or backtrack further. If it has filled in a number in every cell (i.e., there are no more empty cells), the Sudoku is solved, and the function returns True.

2. `valid(board, num, pos)`: This function checks if it's valid to put a certain number in a specific cell. It checks if the number is already present in the same row, column, or 3x3 box.

3. `find_empty(board)`: This function finds the first empty cell in the board, going from left to right and top to bottom.

4. `solve()`: This is a Flask route that serves as the entry point for the application. It receives a POST request with a Sudoku board, solves the Sudoku using the `solve_sudoku(board)` function, and then returns a JSON response with the solved board.

The whole process uses a recursive depth-first search (DFS) approach, which is a common technique for solving problems where you need to find a sequence of actions that leads to a solution, but you don't know the actions in advance. This approach works well for Sudoku because you can build up a solution incrementally (cell by cell), and when you find that a choice you made earlier doesn't work, you can undo it (by "backtracking") and try a different choice.
