from datetime import datetime, timedelta
from pathlib import Path

files: list[Path] = []

for p in Path("/tmp").glob("*"):
    timestamp = p.stat().st_mtime
    ts_date = datetime.fromtimestamp(timestamp)
    delta_max = timedelta(days=1)
    if datetime.now() - ts_date < delta_max:
        files.append(p)

print(files)
