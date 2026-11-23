# Daily script: date_time
# Generated: 2026-11-23T20:43:28.576672

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
