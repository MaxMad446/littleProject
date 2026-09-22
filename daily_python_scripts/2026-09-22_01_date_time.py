# Daily script: date_time
# Generated: 2026-09-22T13:46:52.170535

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
