# Daily script: date_time
# Generated: 2026-09-06T12:28:36.785759

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
