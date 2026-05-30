# Daily script: date_time
# Generated: 2026-05-30T10:44:29.477316

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
