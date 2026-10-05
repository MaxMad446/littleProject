# Daily script: date_time
# Generated: 2026-10-05T17:36:15.672106

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
