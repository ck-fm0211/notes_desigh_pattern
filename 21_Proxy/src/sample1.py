# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Sales(metaclass=ABCMeta):
    """営業interface"""

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def question1():
        pass

    @staticmethod
    @abstractmethod
    def question2():
        pass

    @staticmethod
    @abstractmethod
    def question3():
        pass


class Suzuki(Sales):
    """鈴木さんクラス（本人オブジェクト）"""

    @staticmethod
    def question1():
        print("回答１")

    @staticmethod
    def question2():
        print("回答２")

    @staticmethod
    def question3():
        print("回答３")


class Tanaka(Sales):
    """田中さんクラス（代理人オブジェクト）"""

    @staticmethod
    def question1():
        print("それは「回答１」です")

    @staticmethod
    def question2():
        print("それは「回答２」です")

    @staticmethod
    def question3():
        print("それは「")
        # 答えられないので鈴木先生に聞く
        Suzuki().question3()
        print("」になります")


class Client:
    """お客様クラス"""

    @staticmethod
    def main():
        # 質問１
        Tanaka().question1()

        # 質問２
        Tanaka().question2()

        # 質問３
        Tanaka().question3()


if __name__ == '__main__':
    c = Client()
    c.main()
