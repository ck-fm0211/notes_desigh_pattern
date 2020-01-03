# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Icecream(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def how_sweet(self):
        pass


class VanillaIcecream(Icecream):
    def get_name(self):
        return "バニラアイスクリーム"

    def how_sweet(self):
        return "バニラ味"


class GreenTeaIcecream(Icecream):
    def get_name(self):
        return "抹茶アイスクリーム"

    def how_sweet(self):
        return "抹茶味"


# class CashewNutsVanillaIcecream(Icecream):
#     def get_name(self):
#         return "カシューナッツバニラアイスクリーム"


class CashewNutsToppingIcecream(Icecream):

    def __init__(self, ice: Icecream):
        self._ice = ice

    def get_name(self):
        name = "カシューナッツ"
        name += self._ice.get_name()
        return name

    def how_sweet(self):
        return self._ice.how_sweet()


class SliceAlmondToppingIcecream(Icecream):

    def __init__(self, ice: Icecream):
        self._ice = ice

    def get_name(self):
        name = "スライスアーモンド"
        name += self._ice.get_name()
        return name

    def how_sweet(self):
        return self._ice.how_sweet()


if __name__ == "__main__":
    ice1 = CashewNutsToppingIcecream(VanillaIcecream())  # カシューナッツトッピングのバニラアイス
    ice2 = CashewNutsToppingIcecream(GreenTeaIcecream())  # カシューナッツトッピングの抹茶アイス
    ice3 = SliceAlmondToppingIcecream(CashewNutsToppingIcecream(VanillaIcecream()))  # スライスアーモンド・カシューナッツトッピングのバニラアイス

    print("商品名: {}（{}）".format(ice1.get_name(), ice1.how_sweet()))
    print("商品名: {}（{}）".format(ice2.get_name(), ice2.how_sweet()))
    print("商品名: {}（{}）".format(ice3.get_name(), ice3.how_sweet()))
