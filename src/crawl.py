import csv
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def craw(pagesize=15):
    results = []
    for i in range(5):
        result = requests.get(
            f"https://stackoverflow.com/questions/tagged/python?page={i+1}&pagesize={pagesize}"
        )
        soup = BeautifulSoup(result.content, "lxml")
        for no, tag in enumerate(
            soup.find_all("div", attrs={"class": "question-summary"})
        ):
            question = tag.find("a")
            title = question.contents[0].strip()
            content = tag.find("div", attrs={"class": "excerpt"}).contents[0].strip()
            # content += '"'
            # content: str = content.replace('"', '\\"').replace("\n", "\\n")
            content: str = str(content.encode("utf-8"))[2:-1]

            vote = (
                tag.find("span", attrs={"class": "vote-count-post"})
                .find("strong")
                .contents
            )[0]
            answer = (
                (
                    tag.find("div", attrs={"class": "unanswered"})
                    or tag.find("div", attrs={"class": "answered"})
                    or tag.find("div", attrs={"class": "answered-accepted"})
                )
                .find("strong")
                .contents[0]
            )
            views = (tag.find("div", attrs={"class": "views"}).contents)[0].strip()[:-6]
            result = [
                i * pagesize + no + 1,
                title,
                content,
                int(vote),
                int(answer),
                int(views),
            ]
            results.append(result)

            # print(title)
            # print(content)
            # print(vote)
            # print(answer)
            # print(views)
            # break

    # print("results", results)
    return results
