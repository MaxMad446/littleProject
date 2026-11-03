# Daily script: date_time
# Generated: 2026-11-03T16:43:37.849049

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
