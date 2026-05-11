import os
import json
import logging
import datetime
import subprocess
from datetime import datetime as dt
from datetime import timedelta

def setup_logging():
    """Настраивает систему логирования"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, "daily_commit.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

def get_script_counter(folder, date):
    """Возвращает счетчик скриптов для текущей даты"""
    if not os.path.exists(folder):
        return 1
        
    files = os.listdir(folder)
    today_files = [f for f in files if f.startswith(date)]
    return len(today_files) + 1

def load_used_ideas():
    """Загружает информацию об использованных идеях"""
    if not os.path.exists('used_ideas.json'):
        return {
            "last_used_idea": "",
            "ideas_count": {
                "hello": 0,
                "calculator": 0,
                "random": 0,
                "data_processor": 0,
                "file_manager": 0,
                "api_client": 0,
                "text_generator": 0,
                "math_helper": 0,
                "date_time": 0,
                "string_utils": 0
            }
        }
    
    try:
        with open('used_ideas.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading used_ideas.json: {e}")
        return {
            "last_used_idea": "",
            "ideas_count": {}
        }

def save_used_ideas(used_ideas):
    """Сохраняет информацию об использованных идеях"""
    try:
        with open('used_ideas.json', 'w', encoding='utf-8') as f:
            json.dump(used_ideas, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        logging.error(f"Error saving used_ideas.json: {e}")
        return False

def create_script():
    """Создает новый Python скрипт с уникальным именем и разнообразными идеями"""
    
    # Создаем папку если нет
    folder = "daily_python_scripts"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Получаем текущую дату
    today = dt.now().strftime("%Y-%m-%d")
    
    # Получаем счетчик для сегодняшнего дня
    counter = get_script_counter(folder, today)
    
    # Загружаем информацию об использованных идеях
    used_ideas = load_used_ideas()
    
    # Расширенный список идей для скриптов
    ideas = [
        {
            "name": "hello",
            "code": "print('Hello from daily script!')\nprint(f'Date: {dt.now()}')\n",
            "category": "greeting"
        },
        {
            "name": "calculator", 
            "code": "print('Simple calculator')\nprint(f'2 + 2 = {2+2}')\nprint(f'10 * 5 = {10*5}')\nprint(f'25 / 4 = {25/4}')\n",
            "category": "math"
        },
        {
            "name": "random",
            "code": "import random\nprint(f'Random number: {random.randint(1, 100)}')\nprint(f'Random choice: {random.choice(['apple', 'banana', 'cherry'])}')\n",
            "category": "random"
        },
        {
            "name": "data_processor",
            "code": "import random\ndata = [random.randint(1, 100) for _ in range(10)]\nprint(f'Data: {data}')\nprint(f'Sum: {sum(data)}')\nprint(f'Average: {sum(data) / len(data):.2f}')\n",
            "category": "data"
        },
        {
            "name": "file_manager",
            "code": "import os\nprint(f'Files in current directory:')\nfor file in os.listdir('.'):\n    print(f'  {{file}}')\nprint(f'Current directory: {os.getcwd()}')\n",
            "category": "system"
        },
        {
            "name": "api_client",
            "code": "# Имитация API клиента\nprint('Simulating API request...')\nresponse = {\n    'status': 'success',\n    'data': {\n        'id': 123,\n        'name': 'John Doe',\n        'email': 'john@example.com'\n    }\n}\nprint(f'API Response: {response}')\n",
            "category": "api"
        },
        {
            "name": "text_generator",
            "code": "words = ['hello', 'world', 'python', 'script', 'daily', 'commit']\nimport random\ngenerated_text = ' '.join(random.sample(words, 4))\nprint(f'Generated text: {generated_text}')\n",
            "category": "text"
        },
        {
            "name": "math_helper",
            "code": "import math\nprint(f'Pi: {math.pi:.4f}')\nprint(f'Square root of 16: {math.sqrt(16)}')\nprint(f'Factorial of 5: {math.factorial(5)}')\n",
            "category": "math"
        },
        {
            "name": "date_time",
            "code": "from datetime import datetime, timedelta\nnow = datetime.now()\nprint(f'Current time: {now}')\ntomorrow = now + timedelta(days=1)\nprint(f'Tomorrow: {tomorrow.strftime(\"%Y-%m-%d\")}')\n",
            "category": "datetime"
        },
        {
            "name": "string_utils",
            "code": "text = 'Hello World Python Script'\nprint(f'Original: {text}')\nprint(f'Lowercase: {text.lower()}')\nprint(f'Uppercase: {text.upper()}')\nprint(f'Word count: {len(text.split())}')\n",
            "category": "text"
        }
    ]
    
    # Фильтруем идеи, исключая последнюю использованную
    available_ideas = [idea for idea in ideas if idea['name'] != used_ideas['last_used_idea']]
    
    # Если нет доступных идей (все использованы), сбрасываем последнюю использованную
    if not available_ideas:
        available_ideas = ideas
    
    # Выбираем случайную идею из доступных
    import random
    idea = random.choice(available_ideas)
    
    # Обновляем информацию об использованных идеях
    used_ideas['last_used_idea'] = idea['name']
    if idea['name'] in used_ideas['ideas_count']:
        used_ideas['ideas_count'][idea['name']] += 1
    else:
        used_ideas['ideas_count'][idea['name']] = 1
    
    # Сохраняем обновленную информацию
    save_used_ideas(used_ideas)
    
    # Имя файла с уникальным номером
    filename = f"{today}_{counter:02d}_{idea['name']}.py"
    filepath = os.path.join(folder, filename)
    
    # Проверяем существование файла
    if os.path.exists(filepath):
        logging.warning(f"File already exists: {filename}")
        # Генерируем новое имя с случайным суффиксом
        import random
        suffix = random.randint(100, 999)
        filename = f"{today}_{counter:02d}_{idea['name']}_{suffix}.py"
        filepath = os.path.join(folder, filename)
    
    # Создаем файл
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(idea["code"])
        logging.info(f"Created script: {filename}")
        return filepath
    except Exception as e:
        logging.error(f"Error creating script {filename}: {e}")
        return None

def update_readme():
    """Обновляет README.md с актуальной статистикой"""
    today = dt.now().strftime("%Y-%m-%d")
    
    # Подсчитываем количество скриптов
    script_count = 0
    if os.path.exists("daily_python_scripts"):
        script_count = len([f for f in os.listdir("daily_python_scripts") if f.endswith('.py')])
    
    # Загружаем статистику по идеям
    used_ideas = load_used_ideas()
    total_scripts = sum(used_ideas['ideas_count'].values())
    
    content = f"""# Daily Python Scripts\n\nLast update: {today}\nTotal scripts: {script_count} ({total_scripts} generated)\n\nThis repository is automatically updated daily with new Python scripts.\n\n## Script Ideas Statistics\n"""
    
    for idea, count in used_ideas['ideas_count'].items():
        if count > 0:
            content += f"- {idea}: {count} times\n"
    
    try:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        logging.info("README updated successfully")
    except Exception as e:
        logging.error(f"Error updating README.md: {e}")

def git_commit(filepath):
    """Выполняет git операции с обработкой ошибок"""
    if not filepath:
        logging.error("No file to commit")
        return False
        
    try:
        # Проверяем наличие .git директории
        if not os.path.exists(".git"):
            logging.error("Not a git repository")
            return False
        
        # Добавляем файлы
        result = subprocess.run(["git", "add", filepath], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Git add failed: {result.stderr}")
            return False
        
        result = subprocess.run(["git", "add", "README.md"], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Git add README failed: {result.stderr}")
            return False

        # Проверяем, есть ли что коммитить
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            logging.info("No changes to commit")
            return True
        
        # Коммит
        today = dt.now().strftime("%Y-%m-%d")
        commit_msg = f"🤖 Daily commit: {today}"
        result = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Git commit failed: {result.stderr}")
            return False
        
        # Push
        result = subprocess.run(["git", "push"], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Git push failed: {result.stderr}")
            return False
        
        logging.info("Git operations successful")
        return True
        
    except Exception as e:
        logging.error(f"Git error: {e}")
        return False

def main():
    """Основная функция"""
    # Настраиваем логирование
    setup_logging()
    logging.info("Starting daily commit process")
    
    print("Daily Python Commit")
    print("=" * 40)
    
    # Проверяем git
    if not os.path.exists(".git"):
        logging.error("Error: Not a git repository")
        print("Error: Not a git repository")
        return
    
    # Создаем скрипт
    script_file = create_script()
    
    # Обновляем README
    update_readme()
    
    # Git операции
    if git_commit(script_file):
        logging.info("Daily commit process completed successfully")
        print("Success!")
    else:
        logging.error("Daily commit process failed")
        print("Failed")
    
    # Завершаем работу
    logging.info("Daily commit process finished")

if __name__ == "__main__":
    main()