import tkinter as tk
from generator import create_puzzle
from solver import solve

def create_gui():
    root = tk.Tk()
    root.title("Sudoku")

    # Create Sudoku grid in the GUI
    cells = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            cells[i][j].grid(row=i, column=j)

    def new_game():
        grid = create_puzzle(generate_complete_grid(), difficulty='easy')
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    cells[i][j].insert(0, str(grid[i][j]))
                    cells[i][j].config(state='disabled')
                else:
                    cells[i][j].config(state='normal')
                    cells[i][j].delete(0, tk.END)

    def solve_game():
        grid = [[int(cells[i][j].get()) if cells[i][j].get() else 0 for j in range(9)] for i in range(9)]
        solve(grid)
        for i in range(9):
            for j in range(9):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(grid[i][j]))

    tk.Button(root, text="New Game", command=new_game).grid(row=9, column=0, columnspan=5)
    tk.Button(root, text="Solve", command=solve_game).grid(row=9, column=5, columnspan=4)

    root.mainloop()

