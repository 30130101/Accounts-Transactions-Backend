from .db_data import fetch_dummy_data


def fetch_user_info(customerID):
    users, error = fetch_dummy_data()
    if error:
        return error
    dummy_user = next((user for user in users if user["user_id"] == customerID), None)
    if not dummy_user:
        return f"No user with customer id {customerID} found"
    return dummy_user
