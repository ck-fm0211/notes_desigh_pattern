# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class SaltWater:

    salt = None
    water = None

    @staticmethod
    def salt_water(water, salt):
        SaltWater.salt = salt
        SaltWater.water = water


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def add_solute(self, solute_amount):#溶質を追加
        pass

    @abstractmethod
    def add_solvent(self, solvent_amount):#溶媒を追加
        pass

    @abstractmethod
    def abandon_solution(self, solution_amount):#溶液を捨てる
        pass

    @abstractmethod
    def get_result(self):#生成物を得る
        pass


class Director:

    def __init__(self):

        self.builder = Builder()

    def constract(self):
        self.builder.add_solvent(100)
        self.builder.add_solute(40)
        self.builder.abandon_solution(70)
        self.builder.add_solvent(100)
        self.builder.add_solute(15)


class SaltWaterBuilder(Builder):

    def __init__(self):
        self._salt_water = SaltWater(0,0)

    def add_solute(self, salt_amount):
        self._salt_water.salt += salt_amount

    def add_solvent(self, water_amount):
        self._salt_water.water += water_amount

    def abandon_solution(self, salt_water_amount):
        salt_delta = salt_water_amount * (self._salt_water.salt / (self._salt_water.salt + self._salt_water.water))
        water_delta = salt_water_amount * (self._salt_water.water / (self._salt_water.salt + self._salt_water.water))
        self._salt_water.salt -= salt_delta
        self._salt_water.water -= water_delta

    def get_result(self):
        return self._salt_water






