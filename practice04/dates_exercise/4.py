from datetime import datetime

date1 = datetime(2026, 1, 1, 12, 0, 0)
date2 = datetime(2026, 1, 2, 12, 0, 0)

difference = date2 - date1
print(difference.total_seconds())