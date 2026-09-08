# Daily script: date_time
# Generated: 2026-09-08T13:10:56.190996

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
