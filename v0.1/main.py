import os
import subprocess
import tkinter as tk
from tkinter import messagebox

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

root = tk.Tk()
root.title("Digispark Flasher")

for name, file in firmwares.items():
    btn = tk.Button(root, text=name, command=lambda f=file: flash_firmware(f), width=30)
    btn.pack(pady=5)

root.mainloop()
