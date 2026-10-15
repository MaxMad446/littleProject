# Daily script: date_time
# Generated: 2026-10-15T13:48:17.419759

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
