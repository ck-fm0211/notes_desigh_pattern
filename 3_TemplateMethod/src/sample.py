# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Manual(metaclass=ABCMeta):
    @abstractmethod
    def check_mail(self):
        pass

    @abstractmethod
    def edit_list(self):
        pass

    @abstractmethod
    def send_mail(self):
        pass


class JohnManual(Manual):
    def check_mail(self):
        print("mailアプリでメール確認")

    def edit_list(self):
        print("VBAを使ってリスト修正")

    def send_mail(self):
        print("VBAからそのままメール送信")
