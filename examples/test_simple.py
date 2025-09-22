#!/usr/bin/env python3
"""
Простой тест friendly_exceptions
Simple test of friendly_exceptions
"""

import friendly_exceptions

print("Тест friendly_exceptions")
print("=" * 30)

# Тест KeyError
print("\nТест KeyError:")
try:
    data = {"name": "Alice"}
    print(data["age"])  # Ключ не существует
except KeyError:
    print("KeyError пойман, но объяснение не показано")

# Тест AttributeError
print("\nТест AttributeError:")
try:
    text = "Hello"
    print(text.uppercase())  # Неправильный метод
except AttributeError:
    print("AttributeError пойман, но объяснение не показано")

print("\nТест завершен")
