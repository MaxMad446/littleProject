#!/usr/bin/env python3
"""Ежедневная генерация скрипта — вся логика в одном месте"""
import os, json, random, subprocess
from datetime import datetime, timedelta

IDEAS = [
    "hello", "calculator", "random", "data_processor", "file_manager",
    "api_client", "text_generator", "math_helper", "date_time", "string_utils"
]

SCRIPTS = {
    "hello": 'print("Hello from daily script!")\nprint(f"Date: {datetime.now().date()}")\n',
    "calculator": 'print("Simple calculator")\nprint(f"2 + 2 = {2+2}")\nprint(f"10 * 5 = {10*5}")\n',
    "random": 'import random\nprint(f"Random: {random.randint(1,100)}")\nfruits=["apple","banana","cherry"]\nprint(f"Choice: {random.choice(fruits)}")\n',
    "data_processor": 'import random\ndata=[random.randint(1,100) for _ in range(10)]\nprint(f"Data: {data}")\nprint(f"Sum: {sum(data)}, Avg: {sum(data)/len(data):.2f}")\n',
    "file_manager": 'import os\nprint("Files:")\nfor f in os.listdir("."): print(f" {f}")\n',
    "api_client": 'response={"status":"ok","data":{"id":123}}\nprint(f"API: {response}")\n',
    "text_generator": "words=['hello','world','python']\nimport random\nprint(' '.join(random.sample(words,3)))\n",
    "math_helper": 'import math\nprint(f"Pi: {math.pi:.3f}, sqrt(16)={math.sqrt(16)}, 5!={math.factorial(5)}")\n',
    "date_time": 'from datetime import datetime,timedelta\nnow=datetime.now()\nprint(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")\n',
    "string_utils": "text='Hello World'\nprint(f'Orig: {text}, Lower: {text.lower()}, Upper: {text.upper()}, Words: {len(text.split())}')\n",
}

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("daily_python_scripts", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("backups", exist_ok=True)
    
    # Считаем существующие файлы сегодня
    count = len([f for f in os.listdir("daily_python_scripts") if f.startswith(today) and f.endswith(".py")])
    
    # Выбираем идею (не повторяем последнюю)
    used_file = "used_ideas.json"
    if os.path.exists(used_file):
        with open(used_file) as f:
            used = json.load(f)
        last = used.get("last_used_idea", "")
    else:
        used = {"last_used_idea": "", "ideas_count": {k:0 for k in IDEAS}}
        last = ""
    
    # Выбираем новую идею
    available = [i for i in IDEAS if i != last] or IDEAS
    idea = random.choice(available)
    
    # Создаём скрипт
    filename = f"daily_python_scripts/{today}_{count+1:02d}_{idea}.py"
    with open(filename, "w") as f:
        f.write(f"# Daily script: {idea}\n# Generated: {datetime.now().isoformat()}\n\n")
        f.write(SCRIPTS[idea])
    
    # Обновляем статистику
    used["last_used_idea"] = idea
    used["ideas_count"][idea] = used["ideas_count"].get(idea, 0) + 1
    with open(used_file, "w") as f:
        json.dump(used, f, indent=2)
    
    # Обновляем README
    total_scripts = len([f for f in os.listdir("daily_python_scripts") if f.endswith(".py")])
    total_gen = sum(used["ideas_count"].values())
    stats = "\n".join([f"- {k}: {v} times" for k,v in used["ideas_count"].items() if v > 0])
    
    with open("README.md", "w") as f:
        f.write(f"""# Daily Python Scripts

Last update: {today}
Total scripts: {total_scripts} ({total_gen} generated)

This repository is automatically updated daily with new Python scripts.

## Script Ideas Statistics
{stats}
""")
    
    # Создаём лог
    log_file = f"logs/daily_commit_{today}.log"
    with open(log_file, "w") as f:
        f.write(f"{datetime.now()} - INFO - Generated: {filename}\n")
    
    # Выводим переменные для GitHub Actions
    print(f"::set-output name=file_name::{os.path.basename(filename)}")
    print(f"::set-output name=idea_type::{idea}")
    print(f"::set-output name=today::{today}")
    print(f"✅ Generated: {filename}")

if __name__ == "__main__":
    main()