"""一个使用 tkinter 编写的简易图形界面计算器。"""

import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("简易计算器")
        self.geometry("320x420")
        self.minsize(280, 360)

        self.display = tk.StringVar(value="0")
        self.saved_number = None
        self.pending_operator = None
        self.start_new_number = True

        self.columnconfigure(tuple(range(4)), weight=1)
        self.rowconfigure(0, weight=1)
        for row in range(1, 6):
            self.rowconfigure(row, weight=1)

        entry = ttk.Entry(
            self, textvariable=self.display, justify="right",
            font=("Arial", 24), state="readonly"
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=12)

        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]
        for row_index, values in enumerate(buttons, start=1):
            for column_index, label in enumerate(values):
                ttk.Button(
                    self, text=label, command=lambda key=label: self.press(key)
                ).grid(
                    row=row_index, column=column_index,
                    sticky="nsew", padx=4, pady=4
                )

        self.bind("<Key>", self.on_key)

    def show_number(self, number):
        if not isinstance(number, (int, float)):
            self.display.set(str(number))
        elif not float("-inf") < number < float("inf"):
            self.display.set("错误")
        else:
            self.display.set(f"{number:.12g}")

    def press(self, key):
        if key == "C":
            self.display.set("0")
            self.saved_number = None
            self.pending_operator = None
            self.start_new_number = True
            return

        if key in "0123456789." and len(key) == 1:
            current = self.display.get()
            if self.start_new_number or current == "错误":
                current = "0"
                self.start_new_number = False
            if key == "." and "." in current:
                return
            if key == ".":
                self.display.set(current + ".")
            elif current == "0":
                self.display.set(key)
            else:
                self.display.set(current + key)
            return

        if self.display.get() == "错误":
            return

        if key == "⌫":
            if not self.start_new_number:
                self.display.set(self.display.get()[:-1] or "0")
            return

        if key == "±":
            self.show_number(-float(self.display.get()))
            return

        if key == "%":
            self.show_number(float(self.display.get()) / 100)
            return

        if key in ("+", "-", "×", "÷"):
            if self.pending_operator is not None and not self.start_new_number:
                if not self.calculate():
                    return
            self.saved_number = float(self.display.get())
            self.pending_operator = key
            self.start_new_number = True
            return

        if key == "=" and self.pending_operator is not None:
            self.calculate()
            self.pending_operator = None
            self.saved_number = None
            self.start_new_number = True

    def calculate(self):
        left = self.saved_number
        right = float(self.display.get())
        try:
            if self.pending_operator == "+":
                result = left + right
            elif self.pending_operator == "-":
                result = left - right
            elif self.pending_operator == "×":
                result = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError
                result = left / right
            self.show_number(result)
            if self.display.get() == "错误":
                raise ArithmeticError
            return True
        except (ZeroDivisionError, OverflowError, ArithmeticError):
            self.display.set("错误")
            self.saved_number = None
            self.pending_operator = None
            self.start_new_number = True
            return False

    def on_key(self, event):
        key = event.char
        mapping = {"*": "×", "/": "÷", "\r": "=", "=": "="}
        if key in "0123456789.+-*/=" or key == "\r":
            self.press(mapping.get(key, key))
        elif event.keysym == "BackSpace":
            self.press("⌫")
        elif event.keysym == "Escape":
            self.press("C")


if __name__ == "__main__":
    Calculator().mainloop()
