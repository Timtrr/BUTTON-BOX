import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Словарь с названиями и файлами прошивок
firmwares = {
    "KEY ENTER": "digibutton.ino_enter.hex",
    "Key X": "digibutton.ino_key_X.hex",
    "Key SPACE": "digibutton.ino_space.hex"
}

def flash_firmware(path):
    try:
        messagebox.showinfo("Инструкция", "Подключи Digispark, когда появится запрос.")
        subprocess.run(["micronucleus", "--run", path], check=True)
        messagebox.showinfo("Готово", "Прошивка завершена!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Ошибка", "Прошивка не удалась!")

# Основное окно
root = tk.Tk()
root.title("Digispark Button Box Flasher")
root.geometry("350x250")
root.resizable(False, False)

# Сообщение сверху
label = tk.Label(root, text="Программа прошивает Button Box на назначенную кнопку клавиатуры", wraplength=330, justify="center", font=("Arial", 10, "bold"))
label.pack(pady=15)

# Кнопки прошивки
for name, file in firmwares.items():
    btn = tk.Button(root, text=name, command=lambda f=file: flash_firmware(f), width=35)
    btn.pack(pady=5)

root.mainloop()
