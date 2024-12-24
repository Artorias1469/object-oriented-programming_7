#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, messagebox


def main():
    def open_file():
        filename = entry_filename.get()
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)  # Очистка текстового поля
                text_area.insert(tk.END, content)  # Вставка содержимого файла
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл не найден.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def save_file():
        filename = entry_filename.get()
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                content = text_area.get(1.0, tk.END)  # Получение текста из текстового поля
                file.write(content.strip())  # Сохранение текста в файл
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    # Создание основного окна
    root = tk.Tk()
    root.title("Текстовый редактор")

    # Однострочное текстовое поле для имени файла
    entry_filename = tk.Entry(root, width=50)
    entry_filename.pack(pady=10)

    # Многострочное текстовое поле для содержимого файла
    text_area = tk.Text(root, wrap=tk.WORD, height=15, width=50)
    text_area.pack(pady=10)

    # Кнопки "Открыть" и "Сохранить"
    button_open = tk.Button(root, text="Открыть", command=open_file)
    button_open.pack(side=tk.LEFT, padx=10)

    button_save = tk.Button(root, text="Сохранить", command=save_file)
    button_save.pack(side=tk.LEFT, padx=10)

    # Запуск основного цикла
    root.mainloop()

if __name__ == '__main__':
    main()