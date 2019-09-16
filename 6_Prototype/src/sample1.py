# -*- coding:utf-8 -*-
import copy


def main():
    report1 = Report("title1", "content")
    report2 = copy.deepcopy(report1)

    print("title:", report1.title, report2.title)
    print("content:", report1.content, report2.content)


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content


if __name__ == "__main__":
    main()