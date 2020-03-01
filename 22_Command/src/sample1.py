# -*- coding:utf-8 -*-

ADD_SALT = 1  # 食塩を加えて、かき混ぜる場合
ADD_WATER = 2  # 水を加えて、かき混ぜる場合
MAKE_SALT_WATER = 3  #食塩水を作る場合

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

    def experiment(self, param: int):
        """実験を行うメソッド"""
        if param == ADD_SALT:
            # 食塩を1gずつ加えて飽和食塩水を作る実験をする場合
            # 完全に溶けている間は食塩を加える

            while self.is_melted():
                self.add_salt(1)  # 食塩を1g入れる
                self.mix()  # かき混ぜる

            print("食塩を1gずつ加える実験")
            self.note()

        elif param == ADD_WATER:
            # 水を10gずつ加えて飽和食塩水を作る実験をする場合
            # 溶け残っている間は水を加える

            while not self.is_melted():
                self.add_water(10)  # 水を10g入れる
                self.mix()  # かき混ぜる

            print("水を10gずつ加える実験")
            self.note()

        elif param == MAKE_SALT_WATER:
            # 食塩水を作る実験
            self.mix()
            # 濃度を測り、ノートに記述する
            print("食塩水を作る実験")
            self.note()


class Student:
    """実験する生徒"""

    def main(self):
        # 水100gに食塩を1gずつ加えて飽和食塩水を作る実験
        Beaker(100, 0).experiment(ADD_SALT)

        # 食塩10gに水を10gずつ加えて飽和食塩水を作る実験
        Beaker(0, 10).experiment(ADD_WATER)


if __name__ == '__main__':
    s = Student()
    s.main()
