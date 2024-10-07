from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from service import accounts, users


load_dotenv()
port = int(os.environ.get("PORT"))

app = Flask(__name__)

@app.route("/new_account/<int:customerID>/<initialCredit>")
def new_account(customerID, initialCredit):
    response = accounts.create_account(customerID, int(initialCredit))
    return jsonify(response), 200


@app.route("/user_info/<int:customerID>")
def get_user(customerID):
    response = users.fetch_user_info(customerID)
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True, port=port, host="0.0.0.0")
