# Daily script: date_time
# Generated: 2026-07-13T11:52:58.246692

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
