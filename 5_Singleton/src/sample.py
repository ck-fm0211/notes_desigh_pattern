# -*- coding:utf-8 -*-


class RegisterNote:
    __singleton = None
    __register = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton == None:
            cls.__singleton = super(RegisterNote, cls).__new__(cls)
        return cls.__singleton

    def set_register(self, register=None):
        self.__register = register

    def get_register(self):
        return self.__register

RegisterNote()  # クラス定義の直下に書いて、インスタンスを作るために必ず呼ぶ
