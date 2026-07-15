# Daily script: date_time
# Generated: 2026-07-15T10:42:21.832048

from datetime import datetime,timedelta
now=datetime.now()
print(f"Now: {now}, Tomorrow: {(now+timedelta(days=1)).date()}")
