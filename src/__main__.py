import csv
from datetime import datetime

from .crawl import craw

results = craw()


filename = str(datetime.utcnow())
with open(f"./output/{filename}.csv", "w") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["No", "title", "content", "vote", "answer", "view"])
    writer.writerows(results)
