#!/usr/bin/env python3
"""
🌍 Реальные сценарии использования friendly_exceptions
Real-world scenarios with friendly_exceptions

Этот пример показывает, как библиотека помогает в реальных проектах
This example shows how the library helps in real projects
"""

import friendly_exceptions
import json
import os
from datetime import datetime

print("🌍 Реальные сценарии использования")
print("🌍 Real-world Usage Scenarios")
print("=" * 50)

# Сценарий 1: Работа с API
print("\n1️⃣ Сценарий: Работа с API")
print("1️⃣ Scenario: Working with API")

def process_user_data(api_response):
    """Обработка данных пользователя из API"""
    try:
        # Пытаемся получить данные пользователя
        user_data = api_response["user"]
        username = user_data["username"]
        email = user_data["email"]
        profile = user_data["profile"]
        
        print(f"Пользователь: {username}")
        print(f"Email: {email}")
        print(f"Профиль: {profile}")
        
    except KeyError:
        pass  # friendly_exceptions покажет, какой ключ отсутствует

# Симулируем ответ API с отсутствующими полями
api_response = {
    "user": {
        "username": "alice",
        # "email": "alice@example.com",  # Отсутствует email
        "profile": {"age": 25}
    }
}

process_user_data(api_response)

# Сценарий 2: Работа с файлами
print("\n2️⃣ Сценарий: Работа с файлами")
print("2️⃣ Scenario: Working with files")

def load_config_file(filename):
    """Загрузка конфигурационного файла"""
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
            database_url = config["database"]["url"]
            api_key = config["api"]["key"]
            print(f"Database URL: {database_url}")
            print(f"API Key: {api_key}")
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass  # friendly_exceptions объяснит проблему

# Пытаемся загрузить несуществующий файл
load_config_file("config.json")

# Сценарий 3: Работа с объектами
print("\n3️⃣ Сценарий: Работа с объектами")
print("3️⃣ Scenario: Working with objects")

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.created_at = datetime.now()
    
    def get_info(self):
        return f"{self.name}, {self.age} years old"

def process_user(user_obj):
    """Обработка объекта пользователя"""
    try:
        # Пытаемся получить информацию о пользователе
        info = user_obj.get_info()
        email = user_obj.email  # Атрибут не существует
        print(f"Info: {info}")
        print(f"Email: {email}")
    except AttributeError:
        pass  # friendly_exceptions покажет доступные атрибуты

# Создаем пользователя и пытаемся обработать
user = User("Bob", 30)
process_user(user)

# Сценарий 4: Математические операции
print("\n4️⃣ Сценарий: Математические операции")
print("4️⃣ Scenario: Mathematical operations")

def calculate_average(numbers):
    """Вычисление среднего значения"""
    try:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average
    except (TypeError, ZeroDivisionError):
        pass  # friendly_exceptions объяснит проблему

# Тестируем с разными входными данными
calculate_average([])  # Пустой список
calculate_average(["1", "2", "3"])  # Строки вместо чисел

print("\n✨ Все реальные сценарии обработаны!")
print("✨ All real-world scenarios handled!")
print("\n💡 Совет: friendly_exceptions особенно полезен при разработке и отладке!")
print("💡 Tip: friendly_exceptions is especially useful during development and debugging!")
