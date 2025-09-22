#!/usr/bin/env python3
"""
🖥️ CLI интерфейс friendly_exceptions
CLI interface of friendly_exceptions

Этот пример показывает, как использовать командную строку
This example shows how to use the command line interface
"""

import subprocess
import sys
import os

print("🖥️ Демонстрация CLI интерфейса")
print("🖥️ CLI Interface Demo")
print("=" * 50)

# Проверяем, установлена ли библиотека
try:
    import friendly_exceptions
    print("✅ friendly_exceptions установлена")
    print("✅ friendly_exceptions is installed")
except ImportError:
    print("❌ friendly_exceptions не установлена")
    print("❌ friendly_exceptions is not installed")
    print("💡 Установите: pip install friendly-exceptions")
    print("💡 Install: pip install friendly-exceptions")
    sys.exit(1)

# Функция для запуска CLI команд
def run_cli_command(command):
    """Запуск CLI команды"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except Exception as e:
        return -1, "", str(e)

# Демонстрируем различные CLI команды
cli_commands = [
    ("friendly-exceptions --help", "Показать справку / Show help"),
    ("friendly-exceptions --version", "Показать версию / Show version"),
    ("friendly-exceptions --current-language", "Показать текущий язык / Show current language"),
]

print("\n📋 Доступные CLI команды:")
print("📋 Available CLI commands:")

for command, description in cli_commands:
    print(f"\n🔧 {description}")
    print(f"   Команда / Command: {command}")
    
    returncode, stdout, stderr = run_cli_command(command)
    
    if returncode == 0:
        print("   ✅ Успешно / Success")
        if stdout.strip():
            print(f"   📤 Вывод / Output:\n{stdout}")
    else:
        print("   ❌ Ошибка / Error")
        if stderr.strip():
            print(f"   📤 Ошибка / Error:\n{stderr}")

# Демонстрируем использование в скрипте
print("\n🐍 Использование в Python скрипте:")
print("🐍 Usage in Python script:")

# Создаем временный скрипт для демонстрации
demo_script = '''
import friendly_exceptions

# Демонстрируем ошибку
try:
    data = {"name": "Alice"}
    print(data["age"])  # Отсутствующий ключ
except KeyError:
    pass  # friendly_exceptions автоматически обработает
'''

with open("temp_demo.py", "w", encoding="utf-8") as f:
    f.write(demo_script)

print("   📝 Создан временный скрипт temp_demo.py")
print("   📝 Created temporary script temp_demo.py")

# Запускаем скрипт
print("   🚀 Запускаем скрипт...")
print("   🚀 Running script...")

returncode, stdout, stderr = run_cli_command("python temp_demo.py")

if returncode == 0:
    print("   ✅ Скрипт выполнен успешно")
    print("   ✅ Script executed successfully")
    if stdout.strip():
        print(f"   📤 Вывод / Output:\n{stdout}")
else:
    print("   ❌ Ошибка выполнения")
    print("   ❌ Execution error")
    if stderr.strip():
        print(f"   📤 Ошибка / Error:\n{stderr}")

# Удаляем временный файл
try:
    os.remove("temp_demo.py")
    print("   🗑️ Временный файл удален")
    print("   🗑️ Temporary file removed")
except:
    pass

print("\n✨ CLI интерфейс работает отлично!")
print("✨ CLI interface works great!")
print("\n💡 Совет: Используйте CLI для быстрой настройки!")
print("💡 Tip: Use CLI for quick configuration!")
