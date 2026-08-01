import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"


def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data(file_path=DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "transactions": [],
        }
    except json.JSONDecodeError:
        return {
            "transactions": [],
        }
