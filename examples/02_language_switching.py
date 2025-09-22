#!/usr/bin/env python3
"""
🌍 Переключение языков в friendly_exceptions
Language switching in friendly_exceptions

Этот пример показывает, как переключаться между русским и английским
This example shows how to switch between Russian and English
"""

import friendly_exceptions
from friendly_exceptions import set_language, get_language

print("🌍 Демонстрация переключения языков")
print("🌍 Language Switching Demo")
print("=" * 50)

# Показываем текущий язык
print(f"Текущий язык / Current language: {get_language()}")

# Демонстрируем ошибку на русском
print("\n🇷🇺 Ошибка на русском языке:")
data = {"name": "Алиса"}
print(data["age"])  # Ключ не существует - friendly_exceptions покажет объяснение

# Переключаемся на английский
print("\n🔄 Переключаемся на английский...")
set_language("en")
print(f"Новый язык / New language: {get_language()}")

# Демонстрируем ту же ошибку на английском
print("\n🇺🇸 Same error in English:")
data = {"name": "Alice"}
print(data["age"])  # Key doesn't exist - friendly_exceptions will show explanation

# Переключаемся обратно на русский
print("\n🔄 Переключаемся обратно на русский...")
set_language("ru")
print(f"Язык / Language: {get_language()}")

# Демонстрируем AttributeError на русском
print("\n🇷🇺 AttributeError на русском:")
text = "Привет мир"
print(text.uppercase())  # Неправильный метод - friendly_exceptions покажет правильный

print("\n✨ Языки переключаются легко!")
print("✨ Languages switch easily!")
