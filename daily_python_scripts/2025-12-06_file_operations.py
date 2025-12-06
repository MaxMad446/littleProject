#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: 2025-12-06
Тема: File Operations
"""

import os
from datetime import datetime

# Создание файла
filename = "example.txt"
content = f"""Это тестовый файл.
Создан: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Автоматически сгенерирован."""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Файл '{filename}' создан")

# Чтение файла
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()
    print("Содержимое файла:")
    print("-" * 30)
    print(file_content)
    print("-" * 30)
else:
    print("Файл не найден")

if __name__ == "__main__":
    print("\n" + "="*50)
    print(f"Скрипт: File Operations")
    print(f"Дата: 2025-12-06")
    print("="*50)
