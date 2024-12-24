#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def main():
    def calculate(operation):
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "ошибка"

            label_result.config(text=str(result))
        except ValueError:
            label_result.config(text="ошибка")

    # Создание основного окна
    root = tk.Tk()
    root.title("Простейший калькулятор")

    # Поля ввода
    entry1 = tk.Entry(root)
    entry1.pack()

    entry2 = tk.Entry(root)
    entry2.pack()

    # Кнопки операций
    button_add = tk.Button(root, text="+", command=lambda: calculate("+"), width=20)
    button_add.pack()

    button_subtract = tk.Button(root, text="-", command=lambda: calculate("-"), width=20)
    button_subtract.pack()

    button_multiply = tk.Button(root, text="*", command=lambda: calculate("*"), width=20)
    button_multiply.pack()

    button_divide = tk.Button(root, text="/", command=lambda: calculate("/"), width=20)
    button_divide.pack()

    # Метка для отображения результата
    label_result = tk.Label(root, text="")
    label_result.pack()

    # Запуск основного цикла
    root.mainloop()


if __name__ == "__main__":
    main()