class Alphabet:
    Lang = "UA"
    Letters = ["б","г","ґ","д","ж","з","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ","а","е","є","и","і","ї","о","у","ю","я"]
    def __init__(self, lang = Lang, letters = Letters):
        self.lang = lang
        self.letters = letters
    def  print_alphabet(self):
        print(self.letters)
    def  letters_num(self):
        return len(self.letters)
    def is_ua_lang(self, str: str):
        Letters = ["б", "г", "ґ", "д", "ж", "з", "л", "н", "ф", "ц", "ч", "ш", "щ",
                   "а", "е", "є", "и", "ї", "ю", "я"]
        str = str.lower()
        for i in Letters:
            for j in str:
                if i == j:
                    return "Це українська мова"
                    break
        return "Це не українська мова"
class  EngAlphabet(Alphabet):
    def __init__(self, lang = "En", letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]):
        super().__init__(lang, letters)
        self.__en_letters_num = len(letters)
    def  is_en_letter(self, str:str):
        letters = ["q", "w", "r", "t", "u", "s", "d", "f", "g", "h", "j", "k", "l", "z", "v", "b", "n", "m"]
        str = str.lower()
        if str in letters:
            return "Це англійська літера"
        return "Це не англійська літера"

    def letters_num(self):
        return self.__en_letters_num

    @staticmethod
    def example():
        print("Some text")

test = EngAlphabet()
test.print_alphabet()
print(test.letters_num())
print(test.is_en_letter("J"))
print(test.is_ua_lang("Щ"))
print(EngAlphabet.example())



