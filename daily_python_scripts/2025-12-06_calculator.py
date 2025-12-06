#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: 2025-12-06
Тема: Calculator
"""

def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

print("Простой калькулятор")
print("=" * 30)
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"8 / 2 = {divide(8, 2)}")
print("=" * 30)

if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"Скрипт: Calculator")
    print(f"Дата: 2025-12-06")
    print("="*50)
