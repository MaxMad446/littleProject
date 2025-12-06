#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: 2025-12-06
Тема: List Operations
"""

# Работа со списками
numbers = [1, 2, 3, 4, 5]
print(f"Исходный список: {numbers}")

# Добавление элемента
numbers.append(6)
print(f"После append(6): {numbers}")

# Удаление элемента
numbers.remove(3)
print(f"После remove(3): {numbers}")

# Сортировка
numbers.sort(reverse=True)
print(f"После сортировки по убыванию: {numbers}")

# Списочное выражение
squares = [x**2 for x in range(1, 6)]
print(f"Квадраты чисел от 1 до 5: {squares}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"Скрипт: List Operations")
    print(f"Дата: 2025-12-06")
    print("="*50)
