


class IntoRoman:
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]
    def __init__(self, numb):
        self.__numb = self.arabic_to_roman(numb)
    def arabic_to_roman(self, data):
        t = self.thous[data // 1000]
        h = self.hunds[data // 100 % 10]
        te = self.tens[data // 10 % 10]
        o = self.ones[data % 10]
        return t + h + te + o
    def __str__(self):
        return self.__numb

class IntoArabic:
    rule_add = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    rule_div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
    }
    def __init__(self, numb):
        self.__numb = self.roman_to_arabic(str(numb))
    def roman_to_arabic(self, data):
        number = 0
        prev_literal = None
        for literal in data:
            if prev_literal and self.rule_add[prev_literal] < self.rule_add[literal]:
                number += self.rule_div[(prev_literal, literal)]
            else:
                number += self.rule_add[literal]
            prev_literal = literal
        return number
    def __str__(self):
        return str(self.__numb)


rez = IntoArabic("VIII")
print(rez)