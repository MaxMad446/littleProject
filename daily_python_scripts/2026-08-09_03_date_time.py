# Daily script: date_time
# Generated: 2026-08-09T09:30:05.008337

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
