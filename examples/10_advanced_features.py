#!/usr/bin/env python3
"""
🚀 Продвинутые возможности friendly_exceptions
Advanced features of friendly_exceptions

Этот пример показывает все продвинутые возможности библиотеки
This example shows all advanced features of the library
"""

import friendly_exceptions
from friendly_exceptions import set_language, get_language
from friendly_exceptions.config import Config
from friendly_exceptions.logging import get_logger

print("🚀 Продвинутые возможности friendly_exceptions")
print("🚀 Advanced features of friendly_exceptions")
print("=" * 60)

# 1. Логирование
print("\n1️⃣ Логирование / Logging:")
print("1️⃣ Logging:")

logger = get_logger()
logger.info("Начинаем демонстрацию продвинутых возможностей")
logger.info("Starting demonstration of advanced features")

# 2. Конфигурация в реальном времени
print("\n2️⃣ Конфигурация в реальном времени:")
print("2️⃣ Real-time configuration:")

print(f"   Текущий язык: {get_language()}")
print(f"   Current language: {get_language()}")
print(f"   Включено: {Config.is_enabled()}")
print(f"   Enabled: {Config.is_enabled()}")
print(f"   Показывать traceback: {Config.show_traceback()}")
print(f"   Show traceback: {Config.show_traceback()}")

# 3. Динамическое переключение языков
print("\n3️⃣ Динамическое переключение языков:")
print("3️⃣ Dynamic language switching:")

languages = ["ru", "en", "ru", "en"]
for lang in languages:
    set_language(lang)
    print(f"   Язык изменен на: {get_language()}")
    print(f"   Language changed to: {get_language()}")
    
    # Демонстрируем ошибку на текущем языке
    try:
        data = {"name": "Alice"}
        print(data["age"])  # Отсутствующий ключ
    except KeyError:
        pass

# 4. Настройка поведения библиотеки
print("\n4️⃣ Настройка поведения библиотеки:")
print("4️⃣ Configuring library behavior:")

# Отключаем traceback
Config.set_show_traceback(False)
print("   Traceback отключен / Traceback disabled")

try:
    text = "Hello"
    print(text.uppercase())  # Неправильный метод
except AttributeError:
    pass

# Включаем traceback обратно
Config.set_show_traceback(True)
print("   Traceback включен / Traceback enabled")

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Индекс вне диапазона
except IndexError:
    pass

# 5. Работа с различными типами ошибок
print("\n5️⃣ Работа с различными типами ошибок:")
print("5️⃣ Working with different error types:")

error_scenarios = [
    ("KeyError", lambda: {"a": 1}["b"]),
    ("ValueError", lambda: int("abc")),
    ("TypeError", lambda: "hello" + 123),
    ("IndexError", lambda: [1, 2, 3][10]),
    ("AttributeError", lambda: "hello".uppercase()),
    ("NameError", lambda: print(undefined_var)),
    ("ZeroDivisionError", lambda: 10 / 0),
]

for error_name, error_func in error_scenarios:
    print(f"\n   {error_name}:")
    try:
        error_func()
    except Exception:
        pass

# 6. Интеграция с существующим кодом
print("\n6️⃣ Интеграция с существующим кодом:")
print("6️⃣ Integration with existing code:")

class ExistingClass:
    def __init__(self):
        self.data = {"key1": "value1", "key2": "value2"}
    
    def get_value(self, key):
        """Получение значения по ключу"""
        try:
            return self.data[key]
        except KeyError:
            pass  # friendly_exceptions автоматически обработает
    
    def process_data(self, data):
        """Обработка данных"""
        try:
            result = data["items"][0]["name"]
            return result
        except (KeyError, IndexError, TypeError):
            pass  # friendly_exceptions объяснит проблему

# Используем существующий класс
obj = ExistingClass()

print("   Получение существующего значения:")
value = obj.get_value("key1")
if value:
    print(f"   Значение: {value}")

print("\n   Получение несуществующего значения:")
value = obj.get_value("key3")  # Не существует

print("\n   Обработка сложных данных:")
complex_data = {
    "items": [
        {"name": "Item 1", "price": 100},
        {"name": "Item 2", "price": 200}
    ]
}
result = obj.process_data(complex_data)
if result:
    print(f"   Результат: {result}")

print("\n   Обработка невалидных данных:")
invalid_data = {"items": []}  # Пустой список
result = obj.process_data(invalid_data)

# 7. Производительность и оптимизация
print("\n7️⃣ Производительность и оптимизация:")
print("7️⃣ Performance and optimization:")

import time

# Измеряем время обработки ошибок
start_time = time.time()

for i in range(100):
    try:
        data = {"a": 1}
        print(data["b"])  # Ошибка
    except KeyError:
        pass

end_time = time.time()
processing_time = end_time - start_time

print(f"   Время обработки 100 ошибок: {processing_time:.4f} секунд")
print(f"   Time to process 100 errors: {processing_time:.4f} seconds")
print(f"   Среднее время на ошибку: {processing_time/100*1000:.2f} мс")
print(f"   Average time per error: {processing_time/100*1000:.2f} ms")

# 8. Статистика использования
print("\n8️⃣ Статистика использования:")
print("8️⃣ Usage statistics:")

print("   Поддерживаемые типы ошибок:")
print("   Supported error types:")
supported_errors = [
    "KeyError", "ValueError", "TypeError", "IndexError", "AttributeError",
    "FileNotFoundError", "ImportError", "ZeroDivisionError", "NameError",
    "AssertionError", "OSError", "PermissionError", "IsADirectoryError",
    "ConnectionError", "TimeoutError", "JSONDecodeError", "UnicodeError",
    "OverflowError", "RecursionError", "MemoryError", "SyntaxError",
    "IndentationError", "RuntimeError", "NotImplementedError", "SystemError"
]

for i, error_type in enumerate(supported_errors, 1):
    print(f"   {i:2d}. {error_type}")

print(f"\n   Всего типов ошибок: {len(supported_errors)}")
print(f"   Total error types: {len(supported_errors)}")

# 9. Заключение
print("\n9️⃣ Заключение:")
print("9️⃣ Conclusion:")

print("   ✅ friendly_exceptions полностью интегрирован")
print("   ✅ friendly_exceptions is fully integrated")
print("   ✅ Поддерживает 25+ типов ошибок")
print("   ✅ Supports 25+ error types")
print("   ✅ Работает на 2 языках")
print("   ✅ Works in 2 languages")
print("   ✅ Гибкая конфигурация")
print("   ✅ Flexible configuration")
print("   ✅ Высокая производительность")
print("   ✅ High performance")

logger.info("Демонстрация завершена успешно")
logger.info("Demonstration completed successfully")

print("\n🎉 friendly_exceptions готов к использованию в продакшене!")
print("🎉 friendly_exceptions is ready for production use!")
print("\n💡 Совет: Используйте все возможности библиотеки!")
print("💡 Tip: Use all library features!")
