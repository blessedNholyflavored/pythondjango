#!/usr/bin/python3

class HotBeverage:

    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"
    
    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        txt = ("name : {name}\nprice : {price}\ndescription : {description}")
        return txt.format(name= self.name, price= self.price, description=self.description())

class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.40
        self.name= "coffee"

    def description(self) -> str:
        return "A coffee, to stay awake."

    # def __str__(self) -> str:
    #     txt = ("name: {name}\nprice: {price}\ndescription:{description}")
    #     return txt.format(name= self.name, price=self.price, description=self.description())
    
class Tea(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.30
        self.name= "tea"

    # def description(self) -> str:
    #     return "Just some hot water in a cup."

    # def __str__(self) -> str:
    #     txt = ("name: {name}\nprice: {price}\ndescription:{description}")
    #     return txt.format(name= self.name, price=self.price, description=self.description())

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.50
        self.name= "chocolate"

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."

    # def __str__(self) -> str:
    #     txt = ("name: {name}\nprice: {price}\ndescription:{description}")
    #     return txt.format(name= self.name, price=self.price, description=self.description())


class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.45
        self.name= "cappuccino"

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"

    # def __str__(self) -> str:
    #     txt = ("name: {name}\nprice: {price}\ndescription:{description}")
    #     return txt.format(name= self.name, price=self.price, description=self.description())



def main():
    print(HotBeverage())
    print("\n")
    print(Coffee())
    print("\n")
    print(Tea())
    print("\n")
    print(Chocolate())
    print("\n")
    print(Cappuccino())

if __name__ == '__main__':
    main()