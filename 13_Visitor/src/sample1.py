# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


# 先生クラス
class Teacher(metaclass=ABCMeta):

    def __init__(self, students):
        self._students = students

    @abstractmethod
    def visit(self, student_home):
        getattr(self, 'visit_' + student_home.__class__.__name__.lower())(student_home)

    @abstractmethod
    def get_student_list(self):
        return self._students


# 新人先生クラス
class RookieTeacher(Teacher):

    def __init__(self, students):
        super().__init__(students)

    def visit(self, student_home):
        print("先生：こんにちは")
        super().visit(student_home)

    @staticmethod
    def visit_tanaka(tanaka):
        tanaka.praised_child()

    @staticmethod
    def visit_suzuki(suzuki):
        suzuki.reproved_child()

    def get_student_list(self):
        return self._students


# 家庭クラス
class Home(metaclass=ABCMeta):
    @staticmethod
    def praised_child():
        pass

    @staticmethod
    def reproved_child():
        pass


# 受け入れインタフェース
class TeacherAcceptor(metaclass=ABCMeta):

    def accept(self, teacher: Teacher):
        pass


# 鈴木さんの家庭
class Suzuki(Home, TeacherAcceptor):
    @staticmethod
    def praised_child():
        print("スズキ母：あら、先生ったらご冗談を")

    @staticmethod
    def reproved_child():
        print("スズキ母：うちの子に限ってそんなことは・・・。")

    def accept(self, teacher: Teacher):
        teacher.visit(self.__class__)


# 田中さんの家庭
class Tanaka(Home, TeacherAcceptor):
    @staticmethod
    def praised_child():
        print("タナカ母：あらあら、先生ったらご冗談を")

    @staticmethod
    def reproved_child():
        print("タナカ母：まさか、うちの子に限ってそんなことは・・・。")

    def accept(self, teacher: Teacher):
        teacher.visit(self.__class__)

if __name__ == "__main__":
    rt = RookieTeacher(["suzuki", "tanaka"])

    rt.visit(Suzuki())
    rt.visit(Tanaka())
