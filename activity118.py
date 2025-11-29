class Point:
    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y

    def _str_(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)   # <-- far left, not indented
print(p1)          # <-- far left, not indented