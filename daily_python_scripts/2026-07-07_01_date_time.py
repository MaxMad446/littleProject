# Daily script: date_time
# Generated: 2026-07-07T11:38:38.903395

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
