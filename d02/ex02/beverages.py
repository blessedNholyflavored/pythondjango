#!/usr/bin/python3

def main():
    class HotBeverage:

        def __init__(self) -> None:
            self.price = 0.30
            self.name = "hot beverage"
        
        def description(self) -> str:
            return "Just some hot water in a cup."

        def __str__(self) -> str:
            # return self.name + "\n" + self.price + "\n" + description
            txt = ("name : {name}\n price : {price}\n description : {description}")
            return txt.format(name= self.name, price= self.price, description=self.description())
       

if __name__ == '__main__':
    print(HotBeverage())
    main()