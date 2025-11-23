class myClass:

    __privateVar = 27

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        # Access private variable using myClass_privateVar
        print("Private Variable value:", self.__privateVar)


foo = myClass()
foo.hello()

# This will give error because private methods cannot be accessed directly
# foo.__privMeth()   # ❌ ERROR

# Correct way (name mangling):
