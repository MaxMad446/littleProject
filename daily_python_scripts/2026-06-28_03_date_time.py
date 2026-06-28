# Daily script: date_time
# Generated: 2026-06-28T10:59:03.281791

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
