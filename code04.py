import tkinter as tk
from tkinter import messagebox


def sudoku_solver():
    def perform_sudoku_solution():
        grid = [
            [int(entry.get()) for entry in row]
            for row in sudoku_entries
        ]

        def solve_sudoku(grid):
            empty_cell = find_empty_cell(grid)

            if empty_cell is None:
                return True

            row, col = empty_cell

            for num in range(1, 10):
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                    if solve_sudoku(grid):
                        return True
                    grid[row][col] = 0

            return False

        def find_empty_cell(grid):
            for row in range(9):
                for col in range(9):
                    if grid[row][col] == 0:
                        return (row, col)
            return None

        def is_valid_move(grid, row, col, num):
            return not used_in_row(grid, row, num) and \
                not used_in_col(grid, col, num) and \
                not used_in_box(grid, row - row % 3, col - col % 3, num)

        def used_in_row(grid, row, num):
            for col in range(9):
                if grid[row][col] == num:
                    return True
            return False

        def used_in_col(grid, col, num):
            for row in range(9):
                if grid[row][col] == num:
                    return True
            return False

        def used_in_box(grid, box_start_row, box_start_col, num):
            for row in range(3):
                for col in range(3):
                    if grid[row + box_start_row][col + box_start_col] == num:
                        return True
            return False

        if solve_sudoku(grid):
            messagebox.showinfo("Success", "Sudoku solved successfully!")
            for r in range(9):
                for c in range(9):
                    sudoku_entries[r][c].delete(0, tk.END)
                    sudoku_entries[r][c].insert(0, grid[r][c])
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    sudoku_window = tk.Tk()
    sudoku_window.title("Sudoku Solver")

    sudoku_entries = []
    for r in range(9):
        row_entries = []
        for c in range(9):
            entry = tk.Entry(sudoku_window, width=2)
            entry.grid(row=r, column=c)
            row_entries.append(entry)
        sudoku_entries.append(row_entries)

    tk.Button(sudoku_window, text="Solve Sudoku", command=perform_sudoku_solution).grid(row=9, columnspan=9)

    sudoku_window.mainloop()


if __name__ == "__main__":
    sudoku_solver()
