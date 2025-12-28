class RomanConverter:
    def int_to_roman(self, num):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        i = 0

        while num > 0:
            for _ in range(num // values[i]):
                roman += symbols[i]
                num -= values[i]
            i += 1

        return roman

number = int(input("Enter an integer: "))

obj = RomanConverter()
result = obj.int_to_roman(number)

print("Roman numeral:", result)