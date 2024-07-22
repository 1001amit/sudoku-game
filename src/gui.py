import tkinter as tk
from tkinter import messagebox
from generator import create_puzzle, generate_complete_grid
from solver import solve

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center', validate='key', validatecommand=(root.register(self.validate_input), '%P'), highlightthickness=1) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j)
                self.cells[i][j].bind('<FocusIn>', self.on_focus)
                self.cells[i][j].bind('<FocusOut>', self.on_focus_lost)

        self.difficulty = tk.StringVar(value='easy')
        self.create_buttons()
        self.new_game()

    def validate_input(self, value_if_allowed):
        if value_if_allowed == '' or (value_if_allowed.isdigit() and 1 <= int(value_if_allowed) <= 9):
            return True
        else:
            return False

    def create_buttons(self):
        tk.Button(self.root, text="New Game", command=self.new_game).grid(row=9, column=0, columnspan=5)
        tk.Button(self.root, text="Solve", command=self.solve_game).grid(row=9, column=5, columnspan=4)

        tk.Label(self.root, text="Difficulty:").grid(row=10, column=0, columnspan=2)
        difficulties = ["easy", "medium", "hard"]
        for i, level in enumerate(difficulties):
            tk.Radiobutton(self.root, text=level.capitalize(), variable=self.difficulty, value=level).grid(row=10, column=2+i)

    def new_game(self):
        self.grid = create_puzzle(generate_complete_grid(), difficulty=self.difficulty.get())
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
        if not self.validate_grid(grid):
            messagebox.showerror("Error", "The current grid is invalid and cannot be solved.")
            return
        solve(grid)
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def validate_grid(self, grid):
        for row in grid:
            if not self.is_valid_set(row):
                return False
        for col in range(9):
            if not self.is_valid_set([grid[row][col] for row in range(9)]):
                return False
        for box_row in range(3):
            for box_col in range(3):
                if not self.is_valid_set([grid[r][c] for r in range(box_row * 3, (box_row + 1) * 3) for c in range(box_col * 3, (box_col + 1) * 3)]):
                    return False
        return True

    def is_valid_set(self, values):
        nums = [num for num in values if num != 0]
        return len(nums) == len(set(nums))

    def on_focus(self, event):
        event.widget.config(highlightbackground="blue", highlightcolor="blue")

    def on_focus_lost(self, event):
        event.widget.config(highlightbackground="black", highlightcolor="black")

def create_gui():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

