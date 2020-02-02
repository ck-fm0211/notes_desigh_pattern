# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @staticmethod
    def morning_greet():
        """朝の挨拶"""
        pass

    @staticmethod
    def assign_task():
        """タスクを振る"""
        pass


class BadMoodState(State):

    @staticmethod
    def morning_greet():
        return "おう"

    @staticmethod
    def assign_task():
        return "おい、oooやれって言ったよな？やったのか？"


class GoodMoodState(State):

    @staticmethod
    def morning_greet():
        return "おはよう！今日も頑張ろう！"

    @staticmethod
    def assign_task():
        return "いいね！こないだのoooもいい感じだったよ！この調子で頑張ってね！"


class OrdinaryState(State):

    @staticmethod
    def morning_greet():
        return "おはよう"

    @staticmethod
    def assign_task():
        return "いいね、がんばって"


class StatePatternBoss:

    def __init__(self):
        self.state = None

    def change_state(self, state: State):
        self.state = state

    def morning_greet(self):
        return self.state.morning_greet()

    def assign_task(self):
        return self.state.assign_task()


if __name__ == '__main__':

    boss_state = StatePatternBoss()

    print("===== 1日目：機嫌よし =====")
    boss_state.change_state(OrdinaryState())
    print("部下：おはようございます")
    print(f"上司：{boss_state.morning_greet()}")
    print("部下：今日はxxxやります")
    print(f"上司：{boss_state.assign_task()}")

    print("===== 2日目：機嫌悪い =====")
    boss_state.change_state(BadMoodState())
    print("部下：おはようございます")
    print(f"上司：{boss_state.morning_greet()}")
    print("部下：今日はxxxやります")
    print(f"上司：{boss_state.assign_task()}")

    print("===== 3日目：機嫌良い =====")
    boss_state.change_state(GoodMoodState())    # ここを変更するだけ
    print("部下：おはようございます")
    print(f"上司：{boss_state.morning_greet()}")
    print("部下：今日はxxxやります")
    print(f"上司：{boss_state.assign_task()}")
