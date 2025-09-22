#!/usr/bin/env python3
"""
🎯 Запуск всех примеров friendly_exceptions
Run all friendly_exceptions examples

Этот скрипт запускает все примеры по порядку
This script runs all examples in order
"""

import os
import sys
import subprocess
import time

def run_example(example_file):
    """Запуск примера"""
    print(f"\n{'='*60}")
    print(f"🚀 Запуск: {example_file}")
    print(f"🚀 Running: {example_file}")
    print(f"{'='*60}")
    
    try:
        # Запускаем пример
        result = subprocess.run(
            [sys.executable, example_file],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ Пример выполнен успешно")
            print("✅ Example completed successfully")
            if result.stdout:
                print("\n📤 Вывод / Output:")
                print(result.stdout)
        else:
            print("❌ Ошибка выполнения")
            print("❌ Execution error")
            if result.stderr:
                print("\n📤 Ошибка / Error:")
                print(result.stderr)
    
    except subprocess.TimeoutExpired:
        print("⏰ Время выполнения истекло")
        print("⏰ Execution time expired")
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        print(f"❌ Unexpected error: {e}")
    
    # Пауза между примерами
    time.sleep(2)

def main():
    """Основная функция"""
    print("🎯 Запуск всех примеров friendly_exceptions")
    print("🎯 Running all friendly_exceptions examples")
    print("=" * 60)
    
    # Проверяем, что мы в правильной директории
    if not os.path.exists("01_basic_usage.py"):
        print("❌ Ошибка: Запустите скрипт из папки examples/")
        print("❌ Error: Run the script from the examples/ directory")
        sys.exit(1)
    
    # Список всех примеров в порядке выполнения
    examples = [
        "01_basic_usage.py",
        "02_language_switching.py", 
        "03_smart_suggestions.py",
        "04_all_error_types.py",
        "05_real_world_scenarios.py",
        "06_configuration_demo.py",
        "07_cli_demo.py",
        "08_web_development.py",
        "09_data_science.py",
        "10_advanced_features.py"
    ]
    
    print(f"📋 Найдено примеров: {len(examples)}")
    print(f"📋 Found examples: {len(examples)}")
    
    # Проверяем, какие примеры существуют
    existing_examples = []
    for example in examples:
        if os.path.exists(example):
            existing_examples.append(example)
        else:
            print(f"⚠️  Пример не найден: {example}")
            print(f"⚠️  Example not found: {example}")
    
    print(f"\n✅ Будет запущено примеров: {len(existing_examples)}")
    print(f"✅ Will run examples: {len(existing_examples)}")
    
    # Запускаем все примеры
    for i, example in enumerate(existing_examples, 1):
        print(f"\n📊 Прогресс: {i}/{len(existing_examples)}")
        print(f"📊 Progress: {i}/{len(existing_examples)}")
        run_example(example)
    
    # Итоговая статистика
    print(f"\n{'='*60}")
    print("🎉 Все примеры выполнены!")
    print("🎉 All examples completed!")
    print(f"{'='*60}")
    
    print(f"📊 Статистика / Statistics:")
    print(f"   Всего примеров: {len(existing_examples)}")
    print(f"   Total examples: {len(existing_examples)}")
    print(f"   Время выполнения: ~{len(existing_examples) * 2} секунд")
    print(f"   Execution time: ~{len(existing_examples) * 2} seconds")
    
    print(f"\n💡 Совет: Изучите каждый пример отдельно для лучшего понимания!")
    print(f"💡 Tip: Study each example separately for better understanding!")
    
    print(f"\n🔗 Полезные ссылки / Useful links:")
    print(f"   PyPI: https://pypi.org/project/friendly-exceptions/")
    print(f"   GitHub: https://github.com/artemjs/Pythonlibs")
    print(f"   Документация: https://github.com/artemjs/Pythonlibs/tree/friendly_exceptions/friendly_exceptions%200.0.1")

if __name__ == "__main__":
    main()
