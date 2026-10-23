# Daily script: date_time
# Generated: 2026-10-23T13:57:13.910531

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
