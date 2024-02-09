#!/usr/bin/python3

import sys


def get_item(dict: dict, target: str):
    for key, item in dict.items():
        if key.upper() == target.upper():
            return item
    return None


def get_key(dict: dict, target: str):
    for key, item in dict.items():
        if item.upper() == target.upper():
            return key
    return None


def print_state_or_capital_city(str: str):
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
    value = get_item(states, str)
    key = get_key(capital_cities, str)
    if value:
        print(capital_cities.get(value),
              "is the state of", get_key(states, value))
    elif key:
        print(capital_cities.get(key), "is the capital of", get_key(states, key))
    else:
        print(str, "is neither a capital city nor a state")


def main():
    # if (len(sys.argv) == 2):
    #     return
    tokens = sys.argv[1].split(",")
    print(sys.argv[1])
    for token in tokens:
        token = token.strip()
        if token == "":
            continue
        print_state_or_capital_city(token)


if __name__ == '__main__':
    main()



#     def search_location(*expressions):
#     # Check if the number of expressions is valid
#     if len(expressions) != 1 or not expressions[0]:
#         return

#     # Clean up the input and split expressions
#     expressions = expressions[0].strip().split(',')

#     # Create copies of the dictionaries
#     states_copy = states.copy()
#     capital_cities_copy = capital_cities.copy()

#     results = []

#     for expression in expressions:
#         # Clean up each expression
#         expression = expression.strip().lower()

#         # Check if it's a state
#         if expression in states_copy:
#             results.append(f"{expression} is a state and its capital is {capital_cities_copy[states_copy[expression]]}")

#         # Check if it's a capital
#         elif expression in capital_cities_copy.values():
#             # Find the corresponding state
#             state = [key for key, value in capital_cities_copy.items() if value == expression][0]
#             results.append(f"{expression} is the capital of {state}")

#         # If it's neither a state nor a capital
#         else:
#             results.append(f"{expression} is neither a state nor a capital")

#     # Display the results separated by a carriage return
#     print("\n".join(results))

# # Given dictionaries
# states = {
#     "Oregon": "OR",
#     "Alabama": "AL",
#     "New Jersey": "NJ",
#     "Colorado": "CO"
# }

# capital_cities = {
#     "OR": "Salem",
#     "AL": "Montgomery",
#     "NJ": "Trenton",
#     "CO": "Denver"
# }

# # Example usage
# search_location("Montgomery, Colorado, Paris, Denver, New Jersey")
