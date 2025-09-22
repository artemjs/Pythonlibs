#!/usr/bin/env python3
"""
🧠 Умные подсказки friendly_exceptions
Smart suggestions in friendly_exceptions

Этот пример показывает, как библиотека предлагает похожие имена
This example shows how the library suggests similar names
"""

import friendly_exceptions

print("🧠 Демонстрация умных подсказок")
print("🧠 Smart Suggestions Demo")
print("=" * 50)

# 1. KeyError с похожими ключами
print("\n1️⃣ KeyError с похожими ключами:")
try:
    user_data = {
        "username": "alice",
        "user_id": 123,
        "user_email": "alice@example.com",
        "user_role": "admin"
    }
    print(f"User: {user_data['user_name']}")  # Опечатка: user_name вместо username
except KeyError:
    pass  # friendly_exceptions предложит похожие ключи

# 2. AttributeError с похожими методами
print("\n2️⃣ AttributeError с похожими методами:")
try:
    text = "Hello World"
    print(text.upperr())  # Опечатка: upperr вместо upper
except AttributeError:
    pass  # friendly_exceptions предложит правильный метод

# 3. AttributeError с объектом, у которого много атрибутов
print("\n3️⃣ AttributeError с объектом списка:")
try:
    my_list = [1, 2, 3, 4, 5]
    print(my_list.lenght)  # Опечатка: lenght вместо length
except AttributeError:
    pass  # friendly_exceptions предложит len() или другие методы

# 4. NameError с похожими переменными
print("\n4️⃣ NameError с похожими переменными:")
try:
    # Определяем несколько переменных
    user_name = "Alice"
    user_age = 25
    user_city = "Moscow"
    
    print(f"Hello {user_nam}")  # Опечатка: user_nam вместо user_name
except NameError:
    pass  # friendly_exceptions предложит похожие переменные

# 5. ImportError с похожими модулями
print("\n5️⃣ ImportError с похожими модулями:")
try:
    import jsonn  # Опечатка: jsonn вместо json
except ImportError:
    pass  # friendly_exceptions предложит правильный модуль

print("\n✨ Умные подсказки помогают быстро найти ошибки!")
print("✨ Smart suggestions help quickly find errors!")
