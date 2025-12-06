
"""
Автоматический ежедневный коммит Python скриптов в GitHub
"""

import os
import sys
import json
import random
import datetime
import subprocess
from pathlib import Path

def create_daily_script():
    """Создает ежедневный Python скрипт"""
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    scripts_dir = Path("daily_python_scripts")
    scripts_dir.mkdir(exist_ok=True)
    
    # Простые идеи для скриптов
    ideas = [
        {
            "name": "hello_world",
            "code": '''print("Hello, World!")
print(f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def greet(name):
    """Функция приветствия"""
    return f"Привет, {name}!"

if __name__ == "__main__":
    name = input("Введите ваше имя: ")
    print(greet(name))'''
        },
        {
            "name": "calculator",
            "code": '''def add(a, b):
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
print("=" * 30)'''
        },
        {
            "name": "list_operations",
            "code": '''# Работа со списками
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
print(f"Квадраты чисел от 1 до 5: {squares}")'''
        },
        {
            "name": "file_operations",
            "code": '''import os
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
    print("Файл не найден")'''
        },
        {
            "name": "random_data",
            "code": '''import random
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
print("=" * 30)'''
        }
    ]
    
    # Выбираем случайную идею
    idea = random.choice(ideas)
    
    # Создаем имя файла
    filename = f"{today}_{idea['name']}.py"
    filepath = scripts_dir / filename
    
    # Создаем содержимое файла
    content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ежедневный Python скрипт
Дата: {today}
Тема: {idea['name'].replace('_', ' ').title()}
"""

{idea['code']}

if __name__ == "__main__":
    print("\\n" + "="*50)
    print(f"Скрипт: {idea['name'].replace('_', ' ').title()}")
    print(f"Дата: {today}")
    print("="*50)
'''
    
    # Сохраняем файл
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Создан файл: {filepath}")
    return filepath

def update_readme():
    """Обновляет README.md"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Получаем список скриптов
    scripts_dir = Path("daily_python_scripts")
    if scripts_dir.exists():
        script_files = list(scripts_dir.glob("*.py"))
        script_files.sort(reverse=True)  # Сначала новые
        script_count = len(script_files)
        last_script = script_files[0].stem if script_files else "Нет данных"
    else:
        script_count = 0
        last_script = "Нет данных"
    
    readme_content = f'''# Daily Python Scripts

📅 **Ежедневные Python скрипты**

Автоматическое добавление Python скриптов в GitHub репозиторий.

## 📊 Статистика
- **Всего скриптов:** {script_count}
- **Последнее обновление:** {today}
- **Последний скрипт:** {last_script}

## 🚀 Как использовать

1. Клонируйте репозиторий:
\`\`\`bash
git clone https://github.com/MaxMad446/littleProject.git
cd littleProject
\`\`\`

2. Запустите любой скрипт:
\`\`\`bash
python daily_python_scripts/{last_script}.py
\`\`\`

## 📁 Список скриптов

'''
    
    # Добавляем список скриптов
    if scripts_dir.exists():
        for script in script_files[:10]:  # Последние 10
            readme_content += f"- [{script.stem}](daily_python_scripts/{script.name})\n"
    
    readme_content += f'''
## 🤖 Автоматизация

Скрипты добавляются автоматически каждый день с помощью [daily_commit.py](daily_commit.py).

---

*Обновлено автоматически: {today}*
'''
    
    # Сохраняем README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ README.md обновлен")

def git_operations():
    """Выполняет git операции"""
    try:
        # Добавляем все изменения
        subprocess.run(["git", "add", "."], 
                      check=True, capture_output=True, text=True, encoding='utf-8')
        
        # Коммит
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        commit_msg = f"🤖 Daily commit: {today}"
        subprocess.run(["git", "commit", "-m", commit_msg], 
                      check=True, capture_output=True, text=True, encoding='utf-8')
        
        # Push
        subprocess.run(["git", "push"], 
                      check=True, capture_output=True, text=True, encoding='utf-8')
        
        print(f"✅ Коммит создан: {commit_msg}")
        print("✅ Изменения отправлены на GitHub")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка git: {e}")
        if e.stderr:
            print(f"Детали: {e.stderr}")
        return False

def main():
    """Основная функция"""
    print("=" * 60)
    print("🤖 АВТОМАТИЧЕСКИЙ ЕЖЕДНЕВНЫЙ КОММИТ")
    print("=" * 60)
    
    # Проверяем, что мы в git репозитории
    if not (Path(".") / ".git").exists():
        print("❌ Ошибка: это не git репозиторий!")
        print("Сначала выполните: git init")
        return
    
    try:
        # 1. Создаем скрипт
        print("📝 Создание нового скрипта...")
        script_file = create_daily_script()
        
        # 2. Обновляем README
        print("📄 Обновление README.md...")
        update_readme()
        
        # 3. Git операции
        print("💾 Выполнение git операций...")
        if git_operations():
            print("=" * 60)
            print("🎉 ЗАДАНИЕ ВЫПОЛНЕНО УСПЕШНО!")
            print("=" * 60)
        else:
            print("❌ Произошла ошибка при работе с git")
            
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

