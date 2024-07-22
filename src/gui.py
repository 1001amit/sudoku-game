import tkinter as tk
from generator import create_puzzle, generate_complete_grid
from solver import solve

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j)

        self.create_buttons()
        self.new_game()

    def create_buttons(self):
        tk.Button(self.root, text="New Game", command=self.new_game).grid(row=9, column=0, columnspan=5)
        tk.Button(self.root, text="Solve", command=self.solve_game).grid(row=9, column=5, columnspan=4)

    def new_game(self):
        self.grid = create_puzzle(generate_complete_grid(), difficulty='easy')
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if self.grid[i][j] != 0:
                    self.cells[i][j].insert(0, str(self.grid[i][j]))
                    self.cells[i][j].config(state='disabled')
                else:
                    self.cells[i][j].config(state='normal')

    def solve_game(self):
        grid = [[int(self.cells[i][j].get()) if self.cells[i][j].get() else 0 for j in range(9)] for i in range(9)]
        solve(grid)
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

def create_gui():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

