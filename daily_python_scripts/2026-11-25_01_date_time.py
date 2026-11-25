# Daily script: date_time
# Generated: 2026-11-25T18:54:15.449156

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
