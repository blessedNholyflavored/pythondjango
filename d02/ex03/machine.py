#!/usr/bin/python3

import random
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate

class CoffeeMachine:
    def __init__(self) -> None:
        pass

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.price = "0.90"
            self.name = "empty cup"

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
                def __init__(self) -> None:
                    super().__init__("This coffee machine has to be repaired.")

        def __init__(self) -> None:
            self.count = 10
        
        def repair(self) -> None:
            self.count = 10 

    def serve(self, beverage=HotBeverage) -> HotBeverage():
        if (self.count <= 10):
            raise CoffeeMachine.BrokenMachineException
        self.count -= 1
        if random.random(0, 5) == 0:
            # start stop
            return CoffeeMachine.EmptyCup()
        return beverage()

def test():
    machine = CoffeeMachine()
    for _ in range(100):
        try:
            print(machine.serve(random.choice(
                [Coffee, Tea, Cappuccino, Chocolate])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
        machine.repair()


if __name__ == '__main__':
    test()
   