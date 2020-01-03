# -*- coding:utf-8 -*-


class File:
    def __init__(self, name):
        self._name = name

    def remove(self):
        print("{}を削除しました".format(self._name))


class Directory:
    def __init__(self, name):
        self._name = name
        self._list = []

    def add(self, arg):
        self._list.append(arg)

    def remove(self):
        itr = iter(self._list)

        i = 0

        while next(itr, None) is not None:

            obj = self._list[i]

            if isinstance(obj, File):
                obj.remove()
            elif isinstance(obj, Directory):
                obj.remove()
            else:
                print("削除できません")

            i += 1

        print("{}を削除しました".format(self._name))


if __name__ == "__main__":
    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")
    file4 = File("file4")

    dir1 = Directory("dir1")
    dir1.add(file1)

    dir2 = Directory("dir2")
    dir2.add(file2)
    dir2.add(file3)

    dir1.add(dir2)
    dir1.add(file4)

    dir1.remove()
