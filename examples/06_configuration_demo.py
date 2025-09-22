#!/usr/bin/env python3
"""
⚙️ Конфигурация friendly_exceptions
Configuration of friendly_exceptions

Этот пример показывает, как настроить библиотеку
This example shows how to configure the library
"""

import friendly_exceptions
from friendly_exceptions import set_language, get_language
from friendly_exceptions.config import Config

print("⚙️ Демонстрация конфигурации")
print("⚙️ Configuration Demo")
print("=" * 50)

# Показываем текущие настройки
print("📋 Текущие настройки / Current settings:")
print(f"   Язык / Language: {get_language()}")
print(f"   Включено / Enabled: {Config.is_enabled()}")
print(f"   Показывать traceback / Show traceback: {Config.show_traceback()}")
print(f"   Показывать подсказки / Show suggestions: {Config.show_suggestions()}")

# Демонстрируем ошибку с текущими настройками
print("\n🔍 Демонстрация с текущими настройками:")
try:
    data = {"name": "Alice"}
    print(data["age"])  # Отсутствующий ключ
except KeyError:
    pass

# Изменяем настройки
print("\n⚙️ Изменяем настройки...")
Config.set_show_traceback(False)  # Отключаем traceback
Config.set_show_suggestions(True)  # Включаем подсказки

print("📋 Новые настройки / New settings:")
print(f"   Показывать traceback / Show traceback: {Config.show_traceback()}")
print(f"   Показывать подсказки / Show suggestions: {Config.show_suggestions()}")

# Демонстрируем ошибку с новыми настройками
print("\n🔍 Демонстрация с новыми настройками:")
try:
    text = "Hello"
    print(text.uppercase())  # Неправильный метод
except AttributeError:
    pass

# Переключаем язык
print("\n🌍 Переключаем язык на английский...")
set_language("en")

# Демонстрируем ошибку на английском
print("\n🔍 Демонстрация на английском:")
try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Индекс вне диапазона
except IndexError:
    pass

# Восстанавливаем настройки
print("\n🔄 Восстанавливаем настройки...")
Config.set_show_traceback(True)
set_language("ru")

print("\n✨ Конфигурация работает отлично!")
print("✨ Configuration works great!")
print("\n💡 Совет: Настройте библиотеку под свои нужды!")
print("💡 Tip: Configure the library for your needs!")
