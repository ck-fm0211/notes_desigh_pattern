# -*- coding:utf-8 -*-


class Concierge:

    def __init__(self):
        self._user_dict = {}

    def add_user(self, user: User):
        self._user_dict[user.get_name()] = user

    @staticmethod
    def consultation(colleagueInLove: User, secretLover: User):
        possibility = 0
        # 様々な状況を考慮してpossibilityを導出
        return possibility


class User:
    def __init__(self):
        self._name = None

    def get_name(self):
        return self._name


class John(User):

    def __init__(self):
        super().__init__()
        self._name = "John"
        self._secret_lover = None
        self._tension = None
        self._mediator = Concierge()

    def get_name(self):
        return self._name

    def set_secret_lover(self, user: User):
        self._secret_lover = user

    def needs_advice(self):
        self._tension = self._mediator.consultation(self, self._secret_lover)
