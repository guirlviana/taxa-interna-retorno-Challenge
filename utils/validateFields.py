import imp

def is_valid_fields(object: dict, keys: list):
    for key in keys:
        if key not in object.keys():
            print(f"Your object: {object} is missing the required param: {key}")
            return False
    return True
