import tkinter as tk
from tkinter import messagebox


def convert_temperature():
    def perform_conversion():
        temp = float(entry_temp.get())
        original_unit = entry_unit.get().upper()

        if original_unit == 'C':
            celsius = temp
        elif original_unit == 'F':
            celsius = (temp - 32) * 5 / 9
        elif original_unit == 'K':
            celsius = temp - 273.15
        else:
            messagebox.showerror("Error", "Invalid unit. Please enter C, F, or K.")
            return

        fahrenheit = (celsius * 9 / 5) + 32
        kelvin = celsius + 273.15

        messagebox.showinfo("Converted Temperatures", f"Celsius: {celsius}\nFahrenheit: {fahrenheit}\nKelvin: {kelvin}")

    temp_window = tk.Tk()
    temp_window.title("Temperature Conversion")

    tk.Label(temp_window, text="Enter Temperature:").pack()
    entry_temp = tk.Entry(temp_window)
    entry_temp.pack()

    tk.Label(temp_window, text="Enter Original Unit (C, F, K):").pack()
    entry_unit = tk.Entry(temp_window)
    entry_unit.pack()

    tk.Button(temp_window, text="Convert", command=perform_conversion).pack()

    temp_window.mainloop()


if __name__ == "__main__":
    convert_temperature()
