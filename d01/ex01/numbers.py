#! /usr/bin/env python3

def read_file():
    with open("numbers.txt", "r") as f:
        string = f.read()
        result = string.replace(",", "\n")

        result = result.rstrip("\n")

        print(result)


if __name__ == '__main__':
    read_file()