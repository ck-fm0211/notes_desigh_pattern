# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Editable:
    pass


class Paper(Editable):
    pass


class Manual(metaclass=ABCMeta):

    @abstractmethod
    def edit(self, material: Editable):
        pass

    @abstractmethod
    def create_material(self):
        return Paper()

    @abstractmethod
    def take_memo(self):
        material = self.create_material()
        self.edit(material)


class ElectronicPaper(Editable):
    pass


class JohnManual(Manual):
    def edit(self, material):
        print("電子ペーパーにメモをとる")

    def create_material(self):
        return ElectronicPaper()

    def take_memo(self):
        material = self.create_material()
        self.edit(material)
