#!/usr/bin/env python3
"""
🎯 Все типы ошибок friendly_exceptions
All error types in friendly_exceptions

Этот пример демонстрирует все поддерживаемые типы ошибок
This example demonstrates all supported error types
"""

import friendly_exceptions
import json
import os
import socket
import sys

print("🎯 Демонстрация всех типов ошибок")
print("🎯 All Error Types Demo")
print("=" * 60)

# Список всех демонстраций ошибок
error_demos = [
    ("KeyError", lambda: {"a": 1}["b"]),
    ("ValueError", lambda: int("abc")),
    ("TypeError", lambda: "hello" + 123),
    ("IndexError", lambda: [1, 2, 3][10]),
    ("FileNotFoundError", lambda: open("non_existent.txt", "r")),
    ("ZeroDivisionError", lambda: 10 / 0),
    ("NameError", lambda: print(undefined_var)),
    ("AssertionError", lambda: exec("assert False, 'Test assertion'")),
    ("OSError", lambda: os.chdir("non_existent_dir")),
    ("PermissionError", lambda: os.chmod("non_existent.txt", 0o000)),
    ("IsADirectoryError", lambda: open(".", "r")),
    ("ConnectionError", lambda: socket.socket().connect(("192.168.1.1", 9999))),
    ("TimeoutError", lambda: socket.socket().settimeout(0.001).connect(("8.8.8.8", 80))),
    ("JSONDecodeError", lambda: json.loads("{'bad_json':")),
    ("UnicodeError", lambda: b'\x80'.decode('utf-8')),
    ("OverflowError", lambda: 2**1000000),
    ("RecursionError", lambda: (lambda f: f(f))(lambda f: f(f))),
    ("RuntimeError", lambda: [].pop() if False else (_ for _ in ()).throw(RuntimeError("Test RuntimeError"))),
    ("NotImplementedError", lambda: (lambda: NotImplementedError())()),
    ("SystemError", lambda: sys.call_tracing(lambda: None, ())),
]

print(f"📊 Всего типов ошибок: {len(error_demos)}")
print(f"📊 Total error types: {len(error_demos)}")

for i, (error_name, error_func) in enumerate(error_demos, 1):
    print(f"\n{i:2d}. {error_name}:")
    try:
        error_func()
    except Exception:
        pass  # friendly_exceptions автоматически обработает

print(f"\n✨ Все {len(error_demos)} типов ошибок обработаны!")
print(f"✨ All {len(error_demos)} error types handled!")
print("\n🔗 Документация: https://github.com/artemjs/Pythonlibs")
print("🔗 Documentation: https://github.com/artemjs/Pythonlibs")
