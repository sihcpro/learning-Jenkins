from datetime import datetime
from time import sleep

from . import settings
from .report.stackoverflow import StackOverflowReport

while True:
    kwargs = {
        k: v
        for k, v in dict(
            numOfPage=settings.SOF_NUM_OF_PAGE,
            pageSize=settings.SOF_PAGE_SIZE,
            url=settings.SOF_URL,
            indexColumn=settings.SOF_INDEX_COLUMN,
        ).items()
        if v is not None
    }

    StackOverflowReport(**kwargs).saveAsCsv(
        outputFile=(
            settings.SOF_OUTPUT_FILENAME or f"./output/{str(datetime.utcnow())}.csv"
        )
    )

    sleep(settings.CRAW_EVERY_SECONDS)
