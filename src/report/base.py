import csv

import requests
from bs4 import BeautifulSoup
from requests import Response


class Report:
    def __init__(
        self,
        numOfPage: int,
        pageSize: int,
        url: str,
        outputFile="./output",
        indexColumn=None,
    ):
        self.outputFile = outputFile

        self.url = url
        self.numOfPage = numOfPage
        self.pageSize = pageSize
        self.indexColumn = indexColumn

    def getPageResponse(self, **kwargs) -> Response:
        payload = self.getParams(**kwargs)
        resp = requests.get(self.url, params=payload)
        print("resp", resp.url)
        print("payload", payload)
        return resp

    def getPageSoup(self, **kwargs) -> BeautifulSoup:
        return BeautifulSoup(self.getPageResponse(**kwargs).content, "lxml")

    def getParams(self, **kwargs):
        raise NotImplementedError
        # return kwargs

    @property
    def reportHeader(self):
        raise NotImplementedError

    @property
    def reportBody():
        raise NotImplementedError

    def saveAsCsv(self):
        if self.indexColumn is not None:
            header = [self.indexColumn, *self.reportHeader]
            body = [[i + 1, *values] for i, values in enumerate(self.reportBody)]
        else:
            header = self.reportHeader
            body = self.reportBody

        with open(self.outputFile, "w") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

            writer.writerow(header)
            writer.writerows(body)
