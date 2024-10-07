from clients.transactions_client import create_transaction
from classes.classes import Account, Transaction, User
from .db_data import fetch_dummy_data, set_dummy_data


def create_account(customerID, initialCredit):
    users, error = fetch_dummy_data()
    if error:
        return error
    dummy_user = next((user for user in users if user["user_id"] == customerID), None)
    if not dummy_user:
        return f"No user with customer id {customerID} found"

    user = User(
        id=dummy_user["user_id"],
        name=dummy_user["Name"],
        surname=dummy_user["Surname"],
        balance=dummy_user["balance"],
        accounts=dummy_user["accounts"],
    )

    account = Account([])
    if initialCredit != 0:
        transaction = Transaction(initialCredit)
        try:
            # Call transaction service to create a transaction
            response = create_transaction(transaction)
            if response:
                account.add_transaction(transaction)
                user.update_balance(initialCredit)

            else:
                return "Error while creating transaction", 500
        except Exception as e:
            return f"Error while creating transaction: {e}"

    user.add_account(account)
    set_dummy_data(users, user)
    return account.__dict__
