#!/usr/bin/env python3
"""
🎯 Базовое использование friendly_exceptions
Basic usage of friendly_exceptions

Этот пример показывает, как библиотека автоматически обрабатывает ошибки
This example shows how the library automatically handles errors
"""

# Просто импортируем библиотеку - она автоматически настраивается!
# Just import the library - it automatically sets up!
import friendly_exceptions

print("🚀 Демонстрация friendly_exceptions")
print("=" * 50)

# 1. KeyError - ошибка ключа
print("\n1️⃣ KeyError Example:")
data = {"name": "Alice", "age": 25}
print(f"City: {data['city']}")  # Ключ 'city' не существует - friendly_exceptions покажет объяснение

# 2. AttributeError - ошибка атрибута
print("\n2️⃣ AttributeError Example:")
text = "Hello World"
print(text.uppercase())  # Метод uppercase() не существует - friendly_exceptions покажет правильный метод

# 3. ValueError - ошибка значения
print("\n3️⃣ ValueError Example:")
number = int("abc")  # Нельзя преобразовать "abc" в число - friendly_exceptions объяснит проблему

# 4. TypeError - ошибка типа
print("\n4️⃣ TypeError Example:")
result = "Hello" + 123  # Нельзя сложить строку и число - friendly_exceptions покажет правильный способ

print("\n✨ Все ошибки обработаны с дружелюбными объяснениями!")
print("✨ All errors handled with friendly explanations!")
