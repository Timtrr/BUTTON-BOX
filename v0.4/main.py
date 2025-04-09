import subprocess
import sys
import os
import shutil
import tempfile
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *

# Файлы прошивок
firmwares = {
    "KEY ENTER": "digibutton.ino_enter.hex",
    "Key X": "digibutton.ino_key_X.hex",
    "Key SPACE": "digibutton.ino_space.hex"
}

# Копируем ресурс из упакованного .exe или обычной папки
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

# Загрузка прошивки
def flash_firmware(filename):
    try:
        messagebox.showinfo("Инструкция", "Подключи Digispark, когда появится запрос.")

        temp_dir = tempfile.mkdtemp()
        hex_path = os.path.join(temp_dir, filename)
        exe_path = os.path.join(temp_dir, "micronucleus.exe")

        shutil.copy(resource_path(filename), hex_path)
        shutil.copy(resource_path("micronucleus.exe"), exe_path)

        subprocess.run([exe_path, "--run", hex_path], check=True)
        messagebox.showinfo("Готово", "Прошивка завершена!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Ошибка", "Прошивка не удалась!")

# UI
app = ttk.Window(themename="flatly")
app.title("Digispark Button Box Flasher")
app.geometry("400x300")
app.resizable(False, False)

ttk.Label(app, text="ПРОШИВКА BUTTON BOX", font=("Helvetica", 16, "bold")).pack(pady=(15, 5))
ttk.Label(app, text="Программа прошивает Button Box digispark (pin D0-GND) на назначенную кнопку клавиатуры", wraplength=360, font=("Helvetica", 10), justify="center").pack(pady=(0, 15))

for name, file in firmwares.items():
    ttk.Button(app, text=name, width=30, bootstyle=PRIMARY, command=lambda f=file: flash_firmware(f)).pack(pady=7)

app.mainloop()
