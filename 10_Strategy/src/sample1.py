# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Human:

    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age


class Comparator(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def compare(h1: Human, h2: Human) -> int:
        pass


class AgeComparator(Comparator):

    @staticmethod
    def compare(h1: Human, h2: Human) -> int:
        if h1.age > h2.age:
            return 1
        elif h1.age == h2.age:
            return 0
        else:
            return -1


class HeightComparator(Comparator):

    @staticmethod
    def compare(h1: Human, h2: Human) -> int:
        if h1.height > h2.height:
            return 1
        elif h1.height == h2.height:
            return 0
        else:
            return -1


class SampleClass:

    def __init__(self, comp: Comparator):
        self._comp = comp

    def compare(self, h1: Human, h2: Human) -> int:
        return self._comp.compare(h1, h2)

if __name__ == "__main__":
    h1 = Human("john", 100, 50, 20)
    h2 = Human("Ann", 120, 45, 15)

    ret = SampleClass(AgeComparator()).compare(h1, h2)
    print(ret)  # -> 1
