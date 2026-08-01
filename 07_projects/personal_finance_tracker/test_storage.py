import json

from storage import load_data, save_data


def test_save_data(tmp_path):
    file_path = tmp_path / "test_data.json"

    data = {
        "incomes": [50000, 30000],
        "expenses": [10000],
    }

    save_data(data, file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == data


def test_load_data(tmp_path):
    file_path = tmp_path / "test_data.json"

    data = {
        "incomes": [50000],
        "expenses": [10000],
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    loaded_data = load_data(file_path)

    assert loaded_data == data


def test_load_data_when_file_does_not_exist(tmp_path):
    file_path = tmp_path / "missing.json"

    loaded_data = load_data(file_path)

    assert loaded_data == {
        "incomes": [],
        "expenses": [],
    }


def test_load_invalid_json(tmp_path):
    file_path = tmp_path / "broken.json"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("this is not valid json")

    loaded_data = load_data(file_path)

    assert loaded_data == {
        "incomes": [],
        "expenses": [],
    }
