import tkinter as tk
from tkinter import messagebox
import random


def guessing_game():
    def start_game():
        lower_bound = 1
        upper_bound = 100
        random_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        def guess():
            nonlocal attempts
            user_guess = int(entry_guess.get())
            attempts += 1

            if user_guess < random_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif user_guess > random_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congratulations! You guessed the number in {attempts} attempts.")
                game_window.destroy()

        game_window = tk.Tk()
        game_window.title("Guessing Game")

        tk.Label(game_window, text=f"Guess a number between {lower_bound} and {upper_bound}:").pack()
        entry_guess = tk.Entry(game_window)
        entry_guess.pack()

        tk.Button(game_window, text="Guess", command=guess).pack()

        game_window.mainloop()

    start_game()


if __name__ == "__main__":
    guessing_game()
