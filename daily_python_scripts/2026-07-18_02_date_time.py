# Daily script: date_time
# Generated: 2026-07-18T07:00:16.275820

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
