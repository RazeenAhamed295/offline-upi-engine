import csv
from datetime import datetime

LOG_FILE = "attempts.csv"

def log_attempt(carrier, method, status, reason=""):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            carrier,
            method,
            status,
            reason,
        ])