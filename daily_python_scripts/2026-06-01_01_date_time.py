# Daily script: date_time
# Generated: 2026-06-01T14:52:10.882236

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
