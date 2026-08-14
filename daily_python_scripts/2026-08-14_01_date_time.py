# Daily script: date_time
# Generated: 2026-08-14T09:52:02.840065

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
