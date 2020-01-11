# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Responsible(metaclass=ABCMeta):

    def __init__(self, responsible_person: str):
        self._responsible_person = responsible_person
        self._next_level: Responsible = None

    @abstractmethod
    def set_next(self, next_level):
        self._next_level = next_level
        return self._next_level

    @abstractmethod
    def be_able_to_judge(self, question: Question) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def judge(question: Question):
        pass

    @abstractmethod
    def put_question(self, question: Question):
        if self.be_able_to_judge(question):
            self.judge(question)
        elif self._next_level is not None:
            self._next_level.put_question(question)
        else:
            print("誰にも判断できませんでした。やってみなさい。")


class Question:
    """
    フィールドとして質問の内容を格納するString インスタンスと、
    質問の難易度を表す Level インスタンスを持つ。
    """

    def __init__(self, question: str, level: Level):
        self._question = question
        self._level = level


class Level:
    """
    フィールドとして難易度を表すint型の値と、
    自身の難易度と引数のLevelオブジェクトの難易度を比較するlessThan(Level level)メソッドを持つ
    """

    def __init__(self, level: int):
        self._level: int = level

    def less_than(self, level: Level):
        pass


class RookieTeachee(Responsible):

    def __init__(self, responsible_person):
        super().__init__(responsible_person)
        self._level = Level(2)

    def be_able_to_judge(self, question: Question):
        if question._level.less_than(self._level):
            return True

        return False

    @staticmethod
    def judge(question: Question):
        # ・・・

