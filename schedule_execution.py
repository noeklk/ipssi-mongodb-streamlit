import schedule
import time
from api_fetch_migration import migrate_db

def job():
    migrate_db()
    print("migrated database")

schedule.every(30).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)