# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Sorter(metaclass=ABCMeta)

    @abstractmethod
    def sort(self, obj):
        pass


class QuickSorter(Sorter):

    def sort(self, obj):
        # クイックソート
        pass


class BubbleSorter(Sorter):

    def sort(self, obj):
        # バブルソート
        pass


from datetime import datetime

class TimerSorter(metaclass=ABCMeta, Sorter):

    @abstractmethod
    def time_sorter(self, obj):
        start = datetime.now()
        Sorter.sort(obj)
        end = datetime.now()
        print("time:" + str((end - start)))









