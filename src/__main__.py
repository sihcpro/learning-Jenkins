from datetime import datetime

from .report.stackoverflow import StackOverflowReport

StackOverflowReport(
    numOfPage=1,
    outputFile=f"./output/{str(datetime.utcnow())}.csv",
    indexColumn="No",
).saveAsCsv()
