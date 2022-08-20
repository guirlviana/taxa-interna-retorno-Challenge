import operator

def sort_financial_movement(movement: list, key: str):
    try:
        return movement.sort(key=operator.itemgetter(key))
    except KeyError:
        print(f"The key '{key}' doesn't exists in list")