# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class HotPot:
    pot = None
    soup = None
    protein = None
    vegetables = []
    other_ingredients = []

    @staticmethod
    def hot_pot(pot):
        HotPot.pot = pot

    @staticmethod
    def add_soup(soup):
        HotPot.soup = soup

    @staticmethod
    def add_main(protein):
        HotPot.protein = protein

    @staticmethod
    def add_vegitables(vegitables):
        HotPot.vegetables = vegitables

    @staticmethod
    def add_other_ingredients(other_ingredients):
        HotPot.other_ingredients = other_ingredients


class Factory(metaclass=ABCMeta):

    @abstractmethod
    def get_soup(self):
        pass

    @abstractmethod
    def get_main(self):
        pass

    @abstractmethod
    def get_vegetables(self):
        pass

    @abstractmethod
    def get_other_ingredients(self):
        pass


class MizutakiFactory(Factory):

    def get_soup(self):
        return "torigara"

    def get_main(self):
        return "chicken"

    def get_vegetables(self):
        return ["hakusai", "ninjin", "negi"]

    def get_other_ingredients(self):
        return ["tofu"]


class Sample:


    @staticmethod
    def create_factory(s):
        if s == "キムチ鍋":
            return KimuchiFactory()

        elif s == "すき焼き":
            return SukiyakiFactory()

        else:
            return MizutakiFactory()

    @staticmethod
    def main(arg):
        hp = HotPot()
        fc = create_factory(arg)

        hp.add_soup(fc.get_main())
        hp.add_main(fc.get_main())
        hp.add_vegitables(fc.get_vegetables())
        hp.add_other_ingredients(fc.get_other_ingredients())

