class Computer:

    def _init_(self):
        self.__maxprice = 900   # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setPrice(self, price):
        self.__maxprice = price   # correct way to update private variable


c = Computer()

c.__maxprice = 1000 # ❌ This will NOT change the private variable
c.sell()            # Still 900

c.setPrice(1000)    # ✅ Correct way
c.sell()            # 1000