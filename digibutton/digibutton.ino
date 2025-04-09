#include "DigiKeyboard.h"

#define BUTTON_PIN 0  // Пин D0

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Включаем внутреннюю подтяжку
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW) {  // Кнопка нажата (т.е. замкнута на GND)
    DigiKeyboard.sendKeyStroke(KEY_X); // Отправка Enter
    DigiKeyboard.delay(500); // Задержка, чтобы избежать повторного срабатывания
  }
}