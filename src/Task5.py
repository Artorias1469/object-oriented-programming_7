#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def main():
    def update_label():
        """Обновляет текст метки в зависимости от выбранной радиокнопки."""
        name = selected_option.get()
        if name == 'Егор':
            label.config(text=f"+ 7 (918) 794-98-77")
        elif name == 'Дима':
            label.config(text=f"+ 7 (918) 794-88-77")
        elif name == 'Андрей':
            label.config(text=f"+ 7 (918) 794-90-77")

    # Создание главного окна
    root = tk.Tk()
    root.title("Radiobuttons with indicatoron=0")

    # Переменная для отслеживания выбранной кнопки
    selected_option = tk.StringVar(value="Ничего не выбрано")

    # Метка для отображения информации
    label = tk.Label(root, text="Ничего не выбрано", font=("Arial", 12))
    label.pack(side=tk.RIGHT)

    # Радиокнопки
    options = ["Егор", "Дима", "Андрей"]
    for option in options:
        rb = tk.Radiobutton(
            root,
            text=option,
            value=option,
            variable=selected_option,
            command=update_label,
            indicatoron=0,  # Отключение индикатора
            width=15,
            padx=5,
            pady=5,
            font=15
        )
        rb.pack()

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == '__main__':
    main()