# Daily script: date_time
# Generated: 2026-05-27T12:13:39.900679

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
