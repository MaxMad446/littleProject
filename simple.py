import os
import datetime

# Создаем файл
today = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"daily_python_scripts/{today}.py"

# Создаем папку если нет
os.makedirs("daily_python_scripts", exist_ok=True)

# Пишем в файл
with open(filename, "w") as f:
    f.write(f'print("Script from {today}")')

print(f"File created: {filename}")

# Git команды
os.system(f"git add {filename}")
os.system(f'git commit -m "Daily: {today}"')
os.system("git push")

print("Done")