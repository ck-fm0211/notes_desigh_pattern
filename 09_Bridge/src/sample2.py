# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class SortImple(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, obj):
        pass


class Sorter:
    si = SortImple()

    @staticmethod
    def sorter(si):
        Sorter.si = si

    def sort(self, obj):
        Sorter.si.sort(obj)


class QuickSorterImple(SortImple):

    def sort(self, obj):
        # クイックソート
        pass


class BubbleSorterImple(SortImple):

    def sort(self, obj):
        # バブルソート
        pass


from datetime import datetime


class TimerSorter(metaclass=ABCMeta, Sorter):

    def __init__(self, sort_impl):
        super(sort_impl)

    @abstractmethod
    def time_sorter(self, obj):
        start = datetime.now()
        Sorter.sort(obj)
        end = datetime.now()
        print("time:" + str((end - start)))


