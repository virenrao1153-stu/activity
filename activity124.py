class Reverse:
    def _init_(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

user_input = input("Enter a word: ")

obj = Reverse(user_input)

print("Reversed String:", obj.get_reversed())