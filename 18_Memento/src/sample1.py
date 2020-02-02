# -*- coding:utf-8 -*-


class Memento:
    """途中経過を保持する Memento クラス"""
    result = -1 # 計算の途中経過を表す

    def __init__(self, temp):
        """計算経過を引数に受け取るコンストラクタ"""
        Memento.result = temp


class Calc:
    """ひとつの計算を表すクラス。"""
    temp = 0

    @staticmethod
    def plus(plus):
        """足し算を実行するメソッド"""
        Calc.temp += plus

    @staticmethod
    def create_memento():
        """途中経過を Memento として取得するメソッド"""
        return Memento(Calc.temp)

    @staticmethod
    def set_memento(memento: Memento):
        """Memento から計算経過を取得して、temp にセットする"""
        Calc.temp = memento.result

    @staticmethod
    def get_temp():
        """計算結果を取得するメソッド"""
        return Calc.temp


class Calculator:

    def __init__(self):
        self.result_dict = {}

    def run(self):
        c = Calc()

        # 1回目の計算
        for i in range(1, 6):
            c.plus(i)

        print(f"5までの足し算: {c.get_temp()}")
        self.result_dict["5までの足し算"] = c.create_memento()

        # 2回目の計算
        c2 = Calc()
        c2.set_memento(self.result_dict["5までの足し算"])

        # 1回目の計算
        for i in range(6, 11):
            c2.plus(i)

        print(f"10までの足し算: {c2.get_temp()}")
        self.result_dict["10までの足し算"] = c2.get_temp()


if __name__ == '__main__':
    c = Calculator()
    c.run()
