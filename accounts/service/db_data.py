import os
import json

JSON_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "dummy_data", "dummy_data.json"
)


def fetch_dummy_data():
    try:
        with open(JSON_FILE_PATH, "r") as json_file:
            return json.load(json_file), ""
    except FileNotFoundError:
        return None, "The JSON file was not found."
    except json.JSONDecodeError:
        return None, "Error decoding the JSON file."


def set_dummy_data(users, user):
    with open(JSON_FILE_PATH, "w") as json_file:
        for dummy_user in users:
            if dummy_user["user_id"] == user.id:
                dummy_user["balance"] = user.balance
                dummy_user["accounts"] = user.accounts
                break
        json_file.write(json.dumps(users))
