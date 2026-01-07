from datetime import datetime, timedelta
now = datetime.now()
print(f'Current time: {now}')
tomorrow = now + timedelta(days=1)
print(f'Tomorrow: {tomorrow.strftime("%Y-%m-%d")}')
