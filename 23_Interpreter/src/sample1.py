# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Operand(metaclass=ABCMeta):
    """処理対象を表すインタフェース"""
    @abstractmethod
    def get_operand_string(self):
        pass


class Operator(metaclass=ABCMeta):
    """処理を表すインタフェース"""
    @abstractmethod
    def execute(self):
        pass


class Ingredient(Operand):
    """処理対象を表すクラス"""

    def __init__(self, operand_string: str):
        self._operand_string = operand_string

    def get_operand_string(self) -> str:
        return self._operand_string


class Expression(Operand):
    """処理結果を表すクラス"""

    def __init__(self, operator):
        """処理内容を表す operator を引数に取る"""
        self._operand_string = None
        self._operator = operator

    def get_operand_string(self):
        return self._operator.execute().get_operand_string()


class Plus(Operator):
    """足し合わせる処理を表すクラス"""

    def __init__(self, operand1: Operand, operand2: Operand):
        self._operand1 = operand1
        self._operand2 = operand2

    def execute(self) -> Operand:
        return Ingredient(f"{self._operand1.get_operand_string()}と{self._operand2.get_operand_string()}を足したもの")


class Wait(Operator):
    """「待つ」という処理を表すクラス"""

    def __init__(self, minute: int, operand: Operand):
        self._minute = minute
        self._operand = operand

    def execute(self) -> Operand:
        return Ingredient(f"{self._operand.get_operand_string()}を{self._minute}分置いたもの")


if __name__ == '__main__':
    # 素材
    material1 = Ingredient("麺")
    material2 = Ingredient("粉末スープ")
    material3 = Ingredient("お湯")
    material4 = Ingredient("液体スープ")

    # 工程
    # 麺と粉末スープを入れる
    step1 = Plus(material1, material2).execute()

    # お湯を入れる
    step2 = Plus(step1, material3).execute()

    # 3分待つ
    step3 = Wait(3, step2).execute()

    # 液体スープを入れる
    step4 = Plus(step3, material4).execute()

    print(f"{step4.get_operand_string()}：それがカップラーメン！")
