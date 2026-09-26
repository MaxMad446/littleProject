# Daily script: date_time
# Generated: 2026-09-26T13:29:55.637122

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
