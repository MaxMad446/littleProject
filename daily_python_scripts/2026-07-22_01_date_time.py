# Daily script: date_time
# Generated: 2026-07-22T10:58:46.330742

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
