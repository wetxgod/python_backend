import json

DATA_FILE = "data.json"


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "incomes": [],
            "expenses": [],
        }
    except json.JSONDecodeError:
        return {
            "incomes": [],
            "expenses": [],
        }
