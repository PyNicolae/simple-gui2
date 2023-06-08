import tkinter as tk
from math import pi

class Window(tk.Tk):
    def __init__(self,title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)


def calculeaza():
    input_value = input_field.get()
    try:
        input_value = float(input_value)
        aria = pi * input_value ** 2
    except ValueError:
        aria = "Nu se poate calcula"
    finally:
        value_var.set(aria)


if __name__ == "__main__":
    window = Window("Page", "600x600")

    value_var = tk.StringVar()
    value_var.set("Calculeaza aria cercului")

    label = tk.Label(window, textvariable=value_var)
    label.pack()

    input_field = tk.Entry(window)
    input_field.pack()
    input_field.insert(0,"1")

    button = tk.Button(window, text="Calculeaza", command= calculeaza)
    button.pack()

    window.mainloop()