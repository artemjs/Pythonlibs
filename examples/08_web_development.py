#!/usr/bin/env python3
"""
🌐 Веб-разработка с friendly_exceptions
Web development with friendly_exceptions

Этот пример показывает, как библиотека помогает в веб-разработке
This example shows how the library helps in web development
"""

import friendly_exceptions
import json

print("🌐 Веб-разработка с friendly_exceptions")
print("🌐 Web Development with friendly_exceptions")
print("=" * 50)

# Симуляция веб-фреймворка (Flask/Django style)
class WebApp:
    def __init__(self):
        self.routes = {}
        self.users = {
            "alice": {"id": 1, "email": "alice@example.com", "role": "admin"},
            "bob": {"id": 2, "email": "bob@example.com", "role": "user"}
        }
    
    def get_user(self, username):
        """Получение пользователя по имени"""
        try:
            user = self.users[username]
            return {
                "id": user["id"],
                "email": user["email"],
                "role": user["role"]
            }
        except KeyError:
            pass  # friendly_exceptions покажет доступных пользователей
    
    def process_json_request(self, json_data):
        """Обработка JSON запроса"""
        try:
            data = json.loads(json_data)
            action = data["action"]
            params = data["params"]
            
            if action == "create_user":
                name = params["name"]
                email = params["email"]
                return f"Создан пользователь: {name} ({email})"
            elif action == "update_user":
                user_id = params["user_id"]
                updates = params["updates"]
                return f"Обновлен пользователь {user_id}: {updates}"
            else:
                return f"Неизвестное действие: {action}"
                
        except (json.JSONDecodeError, KeyError, TypeError):
            pass  # friendly_exceptions объяснит проблему

# Создаем веб-приложение
app = WebApp()

print("\n1️⃣ Получение пользователя:")
print("1️⃣ Getting user:")

# Пытаемся получить существующего пользователя
user = app.get_user("alice")
if user:
    print(f"   Пользователь найден: {user}")

# Пытаемся получить несуществующего пользователя
print("\n   Пытаемся получить несуществующего пользователя...")
user = app.get_user("charlie")  # Не существует

print("\n2️⃣ Обработка JSON запросов:")
print("2️⃣ Processing JSON requests:")

# Валидный JSON
valid_json = '{"action": "create_user", "params": {"name": "David", "email": "david@example.com"}}'
print("   Валидный JSON:")
result = app.process_json_request(valid_json)
if result:
    print(f"   Результат: {result}")

# Невалидный JSON
invalid_json = '{"action": "create_user", "params": {"name": "Eve"}'  # Отсутствует закрывающая скобка
print("\n   Невалидный JSON:")
result = app.process_json_request(invalid_json)

# JSON с отсутствующими полями
incomplete_json = '{"action": "update_user", "params": {"user_id": 1}}'  # Отсутствует "updates"
print("\n   JSON с отсутствующими полями:")
result = app.process_json_request(incomplete_json)

print("\n3️⃣ Работа с HTTP заголовками:")
print("3️⃣ Working with HTTP headers:")

def process_headers(headers):
    """Обработка HTTP заголовков"""
    try:
        content_type = headers["Content-Type"]
        authorization = headers["Authorization"]
        user_agent = headers["User-Agent"]
        
        print(f"   Content-Type: {content_type}")
        print(f"   Authorization: {authorization}")
        print(f"   User-Agent: {user_agent}")
        
    except KeyError:
        pass  # friendly_exceptions покажет отсутствующие заголовки

# Симулируем заголовки запроса
request_headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
    # Отсутствует "Authorization"
}

process_headers(request_headers)

print("\n4️⃣ Работа с формами:")
print("4️⃣ Working with forms:")

def validate_form_data(form_data):
    """Валидация данных формы"""
    try:
        username = form_data["username"]
        email = form_data["email"]
        password = form_data["password"]
        confirm_password = form_data["confirm_password"]
        
        if password != confirm_password:
            raise ValueError("Пароли не совпадают")
        
        if len(username) < 3:
            raise ValueError("Имя пользователя слишком короткое")
        
        return True
        
    except (KeyError, ValueError):
        pass  # friendly_exceptions объяснит проблему

# Тестируем валидацию формы
form_data = {
    "username": "al",
    "email": "alice@example.com"
    # Отсутствуют "password" и "confirm_password"
}

validate_form_data(form_data)

print("\n✨ Веб-разработка стала проще с friendly_exceptions!")
print("✨ Web development is easier with friendly_exceptions!")
print("\n💡 Совет: Используйте библиотеку для отладки API и форм!")
print("💡 Tip: Use the library for debugging APIs and forms!")
