class Computer:

    def _init_(self):
        self.__maxprice = 900   # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setPrice(self, price):
        self.__maxprice = price   # correct way to update private variable


c = Computer()
c.sell()             # prints 900

c.__maxprice = 1000  # this does NOT change the private variable
c.sell()             # still prints 900

c.setPrice(1000)     # correct way
c.sell()             # prints 1000