# -*- coding:utf-8 -*-


class HumanLetter:

    def __init__(self, letter):
        self._letter = letter

    def get_letter(self):
        return self._letter


class HumanLetterFactory:
    __singleton = None
    __human_letter = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton is None:
            cls.__singleton = super(HumanLetterFactory, cls).__new__(cls)
        return cls.__singleton

    def __init__(self):
        self.dic = {}

    def get_human_letter(self, letter: str):

        try:
            human_letter = self.dic[letter]
        except KeyError:
            human_letter = HumanLetter(letter)
            self.dic[letter] = human_letter

        return human_letter



class Main:

    @staticmethod
    def take_a_photo(letter: HumanLetter):
        """写真を取る"""
        print(letter.get_letter())

    def main(self):
        """一文字を作成する"""

        # singleton作成
        hlf = HumanLetterFactory()

        a = hlf.get_human_letter("あ")
        self.take_a_photo(a)
        print(a)

        i = hlf.get_human_letter("い")
        self.take_a_photo(i)
        print(i)

        ha = hlf.get_human_letter("は")
        self.take_a_photo(ha)

        a2 = hlf.get_human_letter("あ")
        self.take_a_photo(a2)
        print(a2)

        o = hlf.get_human_letter("お")
        self.take_a_photo(o)
        print(o)

        yo = hlf.get_human_letter("よ")
        self.take_a_photo(yo)

        ri = hlf.get_human_letter("り")
        self.take_a_photo(ri)

        mo = hlf.get_human_letter("も")
        self.take_a_photo(mo)

        a3 = hlf.get_human_letter("あ")
        self.take_a_photo(a3)
        print(a3)

        o2 = hlf.get_human_letter("お")
        self.take_a_photo(o2)
        print(o2)

        i2 = hlf.get_human_letter("い")
        self.take_a_photo(i2)
        print(i2)


if __name__ == '__main__':
    h = Main()
    h.main()
