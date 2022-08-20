def export_to_json(filename: str, cashFlow: dict, tir: float):
    import json
    new_json = {'tir': tir, 'financial_movement': cashFlow}
    new_json = json.dumps(new_json)
    with open(f'{filename}.json', 'w') as json:
        json.write(new_json)