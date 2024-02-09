#! /usr/bin/env python3

def get_state(dict : dict, target: str):
    for key, item in dict.items():
        if key == target:
            # upper?
            return item
    return None

def get_cities(dict : dict, target: str):
    for key, item in dict.items():
        if key == target:
            return item
    return None


def printstuff(str : str):
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

    statevalue = get_state(states, str)
    citiesvalue = get_cities(capital_cities, str)
    if statevalue:
        print(capital_cities.get(statevalue), "is the state of", get_cities(states, statevalue))
    elif citiesvalue:
        print(capital_cities.get(citiesvalue), "is the capital of", get_cities(states, citiesvalue))
    else:
        print(str, "is neither a capital city nor a state")
   
    
def main():
    import sys
    if len(sys.argv) >= 2:
        return
        # print("je rentre")
    var = sys.argv[1].split(",")
    for token in var:
        token = token.strip()
        # print("lol", token)
        if token == "":
            continue
        printstuff(token) 


if __name__ == '__main__':
    main()
