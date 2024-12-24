#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def main():
    def calculate(operation):
        try:
            print(operation)
            if operation == "red":
                result = '#ff0000'
            elif operation == "orange":
                result = '#ff7d00'
            elif operation == "yellow":
                result = '#ffff00'
            elif operation == "green":
                result = '#00ff00'
            elif operation == "blue":
                result = '#007dff'
            elif operation == "blue2":
                result = '#0000ff'
            elif operation == "phioll":
                result = '#7d00ff'

            entry1.config(text=str(result))
        except ValueError:
            entry1.config(text="ошибка")

    # Создание основного окна
    root = tk.Tk()
    root.title("Цвет")
    root.withdraw = 100

    # Поля ввода
    entry1 = tk.Label(root)
    entry1.pack()

    # Кнопки операций
    button_red = tk.Button(root, command=lambda: calculate("red"), width=5, background='#ff0000')
    button_red.pack(side=tk.LEFT)

    button_orange = tk.Button(root, command=lambda: calculate("orange"), width=5, background='#ff7d00')
    button_orange.pack(side=tk.LEFT)

    button_yellow = tk.Button(root, command=lambda: calculate("yellow"), width=5, background='#ffff00')
    button_yellow.pack(side=tk.LEFT)

    button_green = tk.Button(root, command=lambda: calculate("green"), width=5, background='#00ff00')
    button_green.pack(side=tk.LEFT)

    button_blue = tk.Button(root, command=lambda: calculate("blue"), width=5, background='#007dff')
    button_blue.pack(side=tk.LEFT)

    button_blue2 = tk.Button(root, command=lambda: calculate("blue2"), width=5, background='#0000ff')
    button_blue2.pack(side=tk.LEFT)

    button_ = tk.Button(root, command=lambda: calculate("phioll"), width=5, background='#7d00ff')
    button_.pack(side=tk.LEFT)

    # Запуск основного цикла
    root.mainloop()


if __name__ == '__main__':
    main()