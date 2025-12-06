#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: 2025-12-06
Тема: Random Data
"""

import random
import string

def generate_password(length=12):
    """Генерация случайного пароля"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def random_fruit():
    """Случайный фрукт"""
    fruits = ['яблоко', 'банан', 'апельсин', 'виноград', 'манго', 'киви']
    return random.choice(fruits)

print("Генератор случайных данных")
print("=" * 30)
print(f"Случайный пароль: {generate_password(10)}")
print(f"Случайный фрукт: {random_fruit()}")
print(f"Случайное число от 1 до 100: {random.randint(1, 100)}")
print("=" * 30)

if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"Скрипт: Random Data")
    print(f"Дата: 2025-12-06")
    print("="*50)
