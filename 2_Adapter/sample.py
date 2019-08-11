# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Tom:
    def enjoy_with_all_person(self):
        print("enjoy Everyone!!")


class ChairPerson(metaclass=ABCMeta):

    @abstractmethod
    def organize_all(self):
        pass


class Mary(ChairPerson):

    def __init__(self):
        self._tom = Tom()

    def organize_all(self):
        self._tom.enjoy_with_all_person()


# Bossクラスの変更
class Boss:
    def main(self):
        chair_person = Mary()
        chair_person.organize_all()


if __name__ == "__main__":
    b = Boss()
    b.main()

