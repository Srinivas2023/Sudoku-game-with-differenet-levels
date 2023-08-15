import tkinter as tk
import random


easy_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

medium_puzzle = [
    [0, 2, 0, 0, 0, 7, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 1, 6, 0],
    [6, 0, 0, 0, 3, 1, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 7, 0, 0],
    [7, 0, 8, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 5, 0, 0, 0, 6],
    [0, 0, 0, 3, 7, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 1, 0, 0, 0, 0, 0]

]

hard_puzzle = [
    [8, 0, 0, 4, 0, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 1, 0, 0, 0, 0, 6, 5, 0],
    [5, 0, 9, 0, 3, 0, 7, 8, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 4, 8, 0, 2, 0, 1, 0, 3],
    [0, 5, 2, 0, 0, 0, 0, 9, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 9, 0, 2, 0, 0, 5]
]

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.current_level = tk.StringVar(root, "Easy")
        self.level_choices = ["Easy", "Medium", "Hard"]
        self.create_widgets()
        self.generate_puzzle()

    def create_widgets(self):
        self.level_label = tk.Label(self.root, text="Select Level:")
        self.level_label.grid(row=0, column=0)

        self.level_menu = tk.OptionMenu(self.root, self.current_level, *self.level_choices)
        self.level_menu.grid(row=0, column=1)

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.generate_puzzle)
        self.new_game_button.grid(row=0, column=2)

        self.canvas = tk.Canvas(self.root, width=450, height=450, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=1, columnspan=3)

    def generate_puzzle(self):
        self.canvas.delete("all")
        level = self.current_level.get()
        if level == "Easy":
            self.puzzle = self.create_copy(easy_puzzle)
        elif level == "Medium":
            self.puzzle = self.create_copy(medium_puzzle)
        elif level == "Hard":
            self.puzzle = self.create_copy(hard_puzzle)

        self.draw_grid()
        self.draw_puzzle()

    def create_copy(self, puzzle):
        return [row[:] for row in puzzle]

    def draw_grid(self):
        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"
            line_width = 2 if i % 3 == 0 else 1

            x0, y0 = 50 * i, 0
            x1, y1 = 50 * i, 450
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=line_width)

            x0, y0 = 0, 50 * i
            x1, y1 = 450, 50 * i
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=line_width)

    def draw_puzzle(self):
        for row in range(9):
            for col in range(9):
                value = self.puzzle[row][col]
                if value != 0:
                    x, y = col * 50 + 25, row * 50 + 25
                    self.canvas.create_text(x, y, text=str(value), font=("Arial", 20))

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
