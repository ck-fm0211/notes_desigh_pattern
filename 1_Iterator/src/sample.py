# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class Employee:

    def __init__(self, name, sex):
        self._name = name
        self._sex = sex

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex


class NewEmployeeList:

    def __init__(self):
        self._employees = []  # 可変長

    def add(self, employee):
        self._employees.append(employee)

    def get_employee_at(self, idx):
        return self._employees[idx]


class Boss(metaclass=ABCMeta):

    def __init__(self):
        self._employeesList = None

    @abstractmethod
    def create_employee_list(self):
        pass

    @abstractmethod
    def call_employee(self):
        pass

# ここまでが事前に提供されるもの

class Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def iterator(self):
        pass


class Iterator(metaclass=ABCMeta):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class MyEmployeeList(NewEmployeeList, Aggregate): # EmployeeListが変更されたら修正

    def __init__(self):
        super(MyEmployeeList, self).__init__()

    def iterator(self):
        return MyEmployeeIterator(self)

    def get_list_len(self):
        return len(self._employees)


class MyEmployeeIterator(Iterator): # EmployeeListが変更されたら修正

    def __init__(self, employee_list):
        self._index = 0
        self._my_employee_list = employee_list

    def has_next(self):
        if self._my_employee_list.get_list_len() > self._index:
            return True
        else:
            return False

    def next(self):
        emp = self._my_employee_list.get_employee_at(self._index)
        self._index += 1
        return emp

# ここまでがIteratorパターンのために実装したもの

class GoodBoss(Boss): # EmployeeListが変更されても修正の必要がない

    def __init__(self):
        super(GoodBoss, self).__init__()

    def create_employee_list(self):
        self._employeesList = MyEmployeeList()
        self._employeesList.add(Employee("Tom", 1))
        self._employeesList.add(Employee("Mary", 2))
        self._employeesList.add(Employee("Sam", 1))
        self._employeesList.add(Employee("John", 1))
        self._employeesList.add(Employee("Ann", 2))

    def call_employee(self):
        itr = self._employeesList.iterator()
        while itr.has_next():
            print(itr.next().get_name())


def main():
    you = GoodBoss()
    you.create_employee_list()
    you.call_employee()


if __name__ == "__main__":
    main()

