#! /usr/bin/env python3

def capitalcity():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    import sys
    # print (sys.argv[1])
    if len(sys.argv) >= 2:
        x = ' '.join(sys.argv[1:])
    else:
        return
    if x in states:
        y = states.get(x)
        print(capital_cities.get(y))
    else:
        print("Unknown state")


if __name__ == '__main__':
    capitalcity()
