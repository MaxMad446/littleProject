# Daily script: date_time
# Generated: 2026-06-17T12:45:36.917946

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
