#!/usr/bin/env python3
"""
📊 Data Science с friendly_exceptions
Data Science with friendly_exceptions

Этот пример показывает, как библиотека помогает в data science
This example shows how the library helps in data science
"""

import friendly_exceptions
import json

print("📊 Data Science с friendly_exceptions")
print("📊 Data Science with friendly_exceptions")
print("=" * 50)

# Симуляция работы с данными
class DataProcessor:
    def __init__(self):
        self.datasets = {
            "sales": {"rows": 1000, "columns": ["date", "product", "amount", "region"]},
            "users": {"rows": 500, "columns": ["id", "name", "email", "age", "city"]},
            "products": {"rows": 200, "columns": ["id", "name", "price", "category"]}
        }
    
    def load_dataset(self, dataset_name):
        """Загрузка датасета"""
        try:
            dataset = self.datasets[dataset_name]
            print(f"   Датасет '{dataset_name}' загружен:")
            print(f"   Rows: {dataset['rows']}")
            print(f"   Columns: {dataset['columns']}")
            return dataset
        except KeyError:
            pass  # friendly_exceptions покажет доступные датасеты
    
    def analyze_data(self, data, analysis_type):
        """Анализ данных"""
        try:
            if analysis_type == "summary":
                return self._summary_stats(data)
            elif analysis_type == "correlation":
                return self._correlation_analysis(data)
            elif analysis_type == "trend":
                return self._trend_analysis(data)
            else:
                raise ValueError(f"Неизвестный тип анализа: {analysis_type}")
        except (KeyError, ValueError, AttributeError):
            pass  # friendly_exceptions объяснит проблему
    
    def _summary_stats(self, data):
        """Статистика по данным"""
        try:
            rows = data["rows"]
            columns = data["columns"]
            return {
                "total_rows": rows,
                "total_columns": len(columns),
                "column_names": columns
            }
        except (KeyError, TypeError):
            pass
    
    def _correlation_analysis(self, data):
        """Корреляционный анализ"""
        try:
            # Симулируем корреляционный анализ
            numeric_columns = [col for col in data["columns"] if col in ["amount", "price", "age"]]
            return f"Корреляция между {numeric_columns}"
        except (KeyError, AttributeError):
            pass
    
    def _trend_analysis(self, data):
        """Анализ трендов"""
        try:
            if "date" in data["columns"]:
                return "Тренд по дате найден"
            else:
                raise ValueError("Нет колонки с датой для анализа трендов")
        except (KeyError, ValueError):
            pass

# Создаем процессор данных
processor = DataProcessor()

print("\n1️⃣ Загрузка датасетов:")
print("1️⃣ Loading datasets:")

# Загружаем существующий датасет
dataset = processor.load_dataset("sales")

# Пытаемся загрузить несуществующий датасет
print("\n   Пытаемся загрузить несуществующий датасет...")
dataset = processor.load_dataset("inventory")  # Не существует

print("\n2️⃣ Анализ данных:")
print("2️⃣ Data analysis:")

# Анализируем существующий датасет
if dataset:
    print("   Сводная статистика:")
    result = processor.analyze_data(dataset, "summary")
    if result:
        print(f"   Результат: {result}")
    
    print("\n   Корреляционный анализ:")
    result = processor.analyze_data(dataset, "correlation")
    if result:
        print(f"   Результат: {result}")
    
    print("\n   Анализ трендов:")
    result = processor.analyze_data(dataset, "trend")
    if result:
        print(f"   Результат: {result}")

print("\n3️⃣ Работа с JSON данными:")
print("3️⃣ Working with JSON data:")

def process_json_data(json_string):
    """Обработка JSON данных"""
    try:
        data = json.loads(json_string)
        
        # Извлекаем данные
        records = data["records"]
        metadata = data["metadata"]
        
        # Обрабатываем каждую запись
        for record in records:
            id = record["id"]
            value = record["value"]
            timestamp = record["timestamp"]
            
            print(f"   Record {id}: {value} at {timestamp}")
        
        return len(records)
        
    except (json.JSONDecodeError, KeyError, TypeError):
        pass  # friendly_exceptions объяснит проблему

# Валидные JSON данные
valid_json = '''
{
    "metadata": {"source": "sensor", "version": "1.0"},
    "records": [
        {"id": 1, "value": 25.5, "timestamp": "2024-01-01T10:00:00"},
        {"id": 2, "value": 26.1, "timestamp": "2024-01-01T10:01:00"}
    ]
}
'''

print("   Валидные JSON данные:")
count = process_json_data(valid_json)
if count:
    print(f"   Обработано записей: {count}")

# Невалидные JSON данные
invalid_json = '''
{
    "metadata": {"source": "sensor", "version": "1.0"},
    "records": [
        {"id": 1, "value": 25.5, "timestamp": "2024-01-01T10:00:00"},
        {"id": 2, "value": 26.1}
    ]
}
'''

print("\n   Невалидные JSON данные (отсутствует timestamp):")
count = process_json_data(invalid_json)

print("\n4️⃣ Работа с массивами данных:")
print("4️⃣ Working with data arrays:")

def process_data_array(data_array, operation):
    """Обработка массива данных"""
    try:
        if operation == "sum":
            return sum(data_array)
        elif operation == "average":
            return sum(data_array) / len(data_array)
        elif operation == "max":
            return max(data_array)
        elif operation == "min":
            return min(data_array)
        else:
            raise ValueError(f"Неизвестная операция: {operation}")
    except (TypeError, ValueError, ZeroDivisionError):
        pass  # friendly_exceptions объяснит проблему

# Тестируем с валидными данными
data = [1, 2, 3, 4, 5]
print(f"   Данные: {data}")

result = process_data_array(data, "sum")
if result:
    print(f"   Сумма: {result}")

result = process_data_array(data, "average")
if result:
    print(f"   Среднее: {result}")

# Тестируем с невалидными данными
print("\n   Тестируем с невалидными данными:")
result = process_data_array("not_a_list", "sum")  # Не список
result = process_data_array([], "average")  # Пустой список

print("\n✨ Data Science стал проще с friendly_exceptions!")
print("✨ Data Science is easier with friendly_exceptions!")
print("\n💡 Совет: Используйте библиотеку для отладки обработки данных!")
print("💡 Tip: Use the library for debugging data processing!")
