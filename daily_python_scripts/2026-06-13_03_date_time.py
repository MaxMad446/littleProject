# Daily script: date_time
# Generated: 2026-06-13T11:09:26.400758

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
