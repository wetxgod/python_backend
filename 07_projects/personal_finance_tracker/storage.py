import json

DATA_FILE = "data.json"


def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data(file_path=DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
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
