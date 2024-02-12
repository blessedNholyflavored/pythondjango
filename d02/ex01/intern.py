#!/usr/bin/python3

class Intern:

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted"

    def __init__(self, Name=None):
        self.Name = "My name? I’m nobody, an intern, I have no name."

    def __str__(self):
        return self.Name


    def work(self) -> str:
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee():
        return Intern.Coffee()

def main():
    intern = Intern()
    mark = Intern("Mark")
    print(intern)
    print(mark)



if __name__ == '__main__':
    main()