#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: 2025-12-06
Тема: Hello World
"""

print("Hello, World!")
print(f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def greet(name):
    """Функция приветствия"""
    return f"Привет, {name}!"

if __name__ == "__main__":
    name = input("Введите ваше имя: ")
    print(greet(name))

if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"Скрипт: Hello World")
    print(f"Дата: 2025-12-06")
    print("="*50)
