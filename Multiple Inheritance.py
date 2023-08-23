class Mammal:
    def mammal_info(self):
        print("Mammals can give birth")
class WingedMammal:
    def wingedanimalinfo(self):
        print("Winged Animals can flap")
class Bat(Mammal,WingedMammal):
    pass
b1=Bat()
b1.mammal_info()
b1.wingedanimalinfo()