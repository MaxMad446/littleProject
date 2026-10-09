# Daily script: date_time
# Generated: 2026-10-09T15:40:18.366958

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
