# Daily script: date_time
# Generated: 2026-10-17T12:35:16.579915

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
