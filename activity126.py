class A:

    def _init_(self, a):
        self.a = a

    def _eq_(self, other):
        if self.a == other.a:
            return True
        else:
            return False


ob1 = (2)
ob2 = (3)

print("Passed Values :", ob1.a, ob2.a)

ob3 = A(4)
ob4 = A(4)

print("Passed Values :", ob3.a, ob4.a)

print(ob3 == ob4)