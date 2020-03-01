# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Beaker:
    """実験セット"""

    def __init__(self, water: float, salt: float):
        self._water = water
        self._salt = salt
        self._melted = False
        self.mix()

    def mix(self):
        """
        溶液をかき混ぜるメソッド
        溶けたか溶け残ったかをセットする
        常温の飽和食塩水の濃度は約26.4%
        """
        if self.get_density() < 26.4:
            self._melted = True
        else:
            self._melted = False

    def is_melted(self) -> bool:
        return self._melted

    def add_salt(self, salt: float):
        self._salt += salt

    def add_water(self, water: float):
        self._water += water

    def get_density(self):
        return (self._salt/(self._water + self._salt))*100

    def note(self):
        print(f"水：{self._water}g")
        print(f"食塩：{self._salt}g")
        print(f"濃度：{self.get_density()}%")


class Command(metaclass=ABCMeta):
    """実験内容を表すクラスの共通インターフェースを提供するスーパークラス"""

    def __init__(self):
        self._beaker = None

    def set_beaker(self, beaker: Beaker):
        self._beaker = beaker

    def execute(self):
        pass


class AddSaltCommand(Command):
    """食塩を1gずつ加える実験のコマンドクラス"""

    def execute(self):
        while self._beaker.is_melted():
            self._beaker.add_salt(1)
            self._beaker.mix()

        print("食塩を1gずつ加える実験")
        self._beaker.note()


class AddWaterCommand(Command):
    """水を10gずつ加える実験のコマンドクラス"""

    def execute(self):
        while not self._beaker.is_melted():
            self._beaker.add_water(10)
            self._beaker.mix()

        print("水を10gずつ加える実験")
        self._beaker.note()


class MakeSaltWaterCommand(Command):
    """食塩水を作る実験のコマンドクラス"""

    def execute(self):
        self._beaker.mix()

        print("食塩水を作る実験")
        self._beaker.note()


class Student:
    """実験する生徒"""

    def main(self):
        add_salt = AddSaltCommand()
        add_salt.set_beaker(Beaker(100, 0))  # 水100g入ったビーカーを用意する

        add_water = AddWaterCommand()
        add_water.set_beaker(Beaker(10, 10))  # 食塩10g入ったビーカーを用意する

        make_saltwater = MakeSaltWaterCommand()
        make_saltwater.set_beaker(Beaker(90, 10))  # 水90g、食塩10g入ったビーカーを用意する

        add_salt.execute()  # 水100gに食塩を1gずつ加えて飽和食塩水を作る実験

        add_water.execute()  # 食塩10gに水を10gずつ加えて飽和食塩水を作る実験

        make_saltwater.execute()  # 10%の食塩水100gを作る実験


if __name__ == '__main__':
    s = Student()
    s.main()
