pyinstaller --noconfirm --windowed --onefile ^
--add-data "digibutton.ino_enter.hex;." ^
--add-data "digibutton.ino_key_X.hex;." ^
--add-data "digibutton.ino_space.hex;." ^
--add-data "micronucleus.exe;." ^
main.py
pause