# -*- coding:utf-8 -*-

import copy


class Product(object):
    def use(self, s):
        pass

    def createClone(self):
        pass


class Manager(object):
    __showcase = dict()

    def register(self, name, proto):
        self.__showcase[name] = proto

    def create(self, protoname):
        p = self.__showcase.get(protoname)
        return p.createClone()


class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        length = len(s)
        deco = self.decochar * (length + 4)
        print(deco)
        print(self.decochar, s, self.decochar)
        print(deco)

    def createClone(self):
        p = copy.deepcopy(self)
        return p


class Underline(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        length = len(s)
        print('"%s"' % s)
        print(" %s " % (self.ulchar * length))

    def createClone(self):
        p = copy.deepcopy(self)
        return p


if __name__ == "__main__":
    manager = Manager()
    uline = Underline("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    pbox = MessageBox("+")
    uline2 = Underline("=")
    manager.register("strong message", uline)
    manager.register("star box", mbox)
    manager.register("slash box", sbox)
    manager.register("plus box", pbox)
    manager.register("under line", uline2)

    p1 = manager.create("strong message")
    p1.use("Hello, world.")
    p2 = manager.create("star box")
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    p3.use("Hello, world.")
    p4 = manager.create("plus box")
    p4.use("Hello, world.")
    p5 = manager.create("under line")
    p5.use("Hello, world.")
