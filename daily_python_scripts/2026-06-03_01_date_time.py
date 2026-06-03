# Daily script: date_time
# Generated: 2026-06-03T13:08:49.216325

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
