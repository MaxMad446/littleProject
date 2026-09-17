# Daily script: date_time
# Generated: 2026-09-17T13:57:54.200241

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
