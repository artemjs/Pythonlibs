#!/usr/bin/env python3
"""
Отладочный тест friendly_exceptions
Debug test for friendly_exceptions
"""

import friendly_exceptions
import sys
import traceback

print("🔍 Отладочный тест friendly_exceptions")
print("=" * 50)

# Проверяем настройки
print(f"Версия: {friendly_exceptions.__version__}")
print(f"Язык: {friendly_exceptions.get_language()}")
print(f"excepthook: {sys.excepthook}")

# Тестируем KeyError
print("\n🔍 Тест KeyError:")
try:
    data = {"name": "Alice"}
    print(data["age"])  # Ключ не существует
except KeyError as e:
    print(f"KeyError пойман: {e}")
    print("Тип ошибки:", type(e))
    print("Traceback:")
    traceback.print_exc()

# Тестируем AttributeError
print("\n🔍 Тест AttributeError:")
try:
    text = "Hello"
    print(text.uppercase())  # Неправильный метод
except AttributeError as e:
    print(f"AttributeError пойман: {e}")
    print("Тип ошибки:", type(e))
    print("Traceback:")
    traceback.print_exc()

print("\n🔍 Тест завершен")
