# -*- coding:utf-8 -*-


class HumanLetter:

    def __init__(self, letter):
        self._letter = letter

    def get_letter(self):
        return self._letter


class Main:

    @staticmethod
    def take_a_photo(letter: HumanLetter):
        """写真を取る"""
        print(letter.get_letter())

    def main(self):
        """一文字を作成する"""
        a = HumanLetter("あ")
        self.take_a_photo(a)

        i = HumanLetter("い")
        self.take_a_photo(i)

        ha = HumanLetter("は")
        self.take_a_photo(ha)

        self.take_a_photo(a)

        o = HumanLetter("お")
        self.take_a_photo(o)

        yo = HumanLetter("よ")
        self.take_a_photo(yo)

        ri = HumanLetter("り")
        self.take_a_photo(ri)

        mo = HumanLetter("も")
        self.take_a_photo(mo)

        self.take_a_photo(a)

        self.take_a_photo(o)

        self.take_a_photo(i)


if __name__ == '__main__':
    h = Main()
    h.main()
