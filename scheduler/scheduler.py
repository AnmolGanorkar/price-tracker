# Scheduler script
# TODO: Implement scheduling logic with APScheduler or cron

import schedule
import time
import subprocess

def run_pipeline():
    print("Running pipeline...")

    subprocess.run(["python", "scraper/scraper.py"])
    subprocess.run(["python", "processing/clean_data.py"])
    subprocess.run(["python", "database/db.py"])

    print("Pipeline completed")

schedule.every(6).hours.do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)