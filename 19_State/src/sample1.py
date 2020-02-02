# -*- coding:utf-8 -*-


class Boss:
    STATE_ORDINARY = 0  # 通常時の上司
    STATE_IN_BAD_MOOD = 1   # 機嫌の悪い上司

    def __init__(self):
        self.state = -1  # 上司の状態を表す

    def change_state(self, state):
        """上司の状態を変更する"""
        self.state = state

    def morning_greet(self):
        """朝の挨拶を返す"""
        if self.state == Boss.STATE_ORDINARY:
            return "おはよう"
        elif self.state == Boss.STATE_IN_BAD_MOOD:
            return "おう"
        else:
            pass

    def assign_task(self):
        """タスクを振る"""
        if self.state == Boss.STATE_ORDINARY:
            return "いいね、がんばって"
        elif self.state == Boss.STATE_IN_BAD_MOOD:
            return "おい、oooやれって言ったよな？やったのか？"
        else:
            pass
