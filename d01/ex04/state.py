#! /usr/bin/env python3

def capitalcity():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    import sys

    if len(sys.argv) >= 2:
        x = ' '.join(sys.argv[1:])
    else:
        return

    matching_state = None
    for state, capital in states.items():
        if capital_cities[capital] == x:
            matching_state = state
            break

    if matching_state:
        print(matching_state)
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    capitalcity()
