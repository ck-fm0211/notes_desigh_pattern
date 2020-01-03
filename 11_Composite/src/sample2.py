# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class DirectoryEntry(metaclass=ABCMeta):
    @abstractmethod
    def remove(self):
        pass


class File(DirectoryEntry):
    def __init__(self, name):
        self._name = name

    def remove(self):
        print("{}を削除しました".format(self._name))


class Directory(DirectoryEntry):
    def __init__(self, name):
        self._name = name
        self._list = []

    def add(self, entry: DirectoryEntry):
        self._list.append(entry)

    def remove(self):
        itr = iter(self._list)

        i = 0

        while next(itr, None) is not None:

            obj = self._list[i]
            obj.remove()

            i += 1

        print("{}を削除しました".format(self._name))


class SymbolicLink(DirectoryEntry):
    def __init__(self, name):
        self._name = name

    def remove(self):
        print("{}を削除しました".format(self._name))


if __name__ == "__main__":
    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")
    file4 = File("file4")
    sym1 = SymbolicLink("sym1")
    sym2 = SymbolicLink("sym2")

    dir1 = Directory("dir1")
    dir1.add(file1)
    dir1.add(sym1)

    dir2 = Directory("dir2")
    dir2.add(file2)
    dir2.add(file3)
    dir2.add(sym2)

    dir1.add(dir2)
    dir1.add(file4)

    dir1.remove()
