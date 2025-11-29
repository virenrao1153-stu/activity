from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self, x):
        print("Passed value:", x)

    @abstractmethod
    def task(self):
        pass   # abstract methods cannot have a body


class test_class(Absclass):

    def task(self):
        print("We are inside test_class task")


# object creation
test_obj = test_class()

test_obj.task()
test_obj.print(100)