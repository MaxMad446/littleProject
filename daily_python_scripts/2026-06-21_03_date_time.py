# Daily script: date_time
# Generated: 2026-06-21T11:39:05.790919

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
