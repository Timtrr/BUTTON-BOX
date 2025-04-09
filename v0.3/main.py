import subprocess
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox  # Используем стандартный messagebox

# Список прошивок
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

# Окно
app = ttk.Window(themename="flatly")
app.title("Digispark Button Box Flasher")
app.geometry("400x300")
app.resizable(False, False)

# Заголовок
ttk.Label(
    app,
    text="ПРОШИВКА BUTTON BOX",
    font=("Helvetica", 16, "bold"),
    anchor="center"
).pack(pady=(15, 5))

# Подзаголовок
ttk.Label(
    app,
    text="Программа прошивает Button Box на назначенную кнопку клавиатуры",
    wraplength=360,
    font=("Helvetica", 10),
    anchor="center",
    justify="center"
).pack(pady=(0, 15))

# Кнопки
for name, file in firmwares.items():
    ttk.Button(app, text=name, width=30, bootstyle=PRIMARY, command=lambda f=file: flash_firmware(f)).pack(pady=7)

app.mainloop()
