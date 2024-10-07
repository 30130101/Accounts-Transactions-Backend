from flask import Flask, request
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5001))


@app.route("/create_transaction", methods=["POST"])
def create_transaction():
    data = request.json
    print(data)
    return "Transaction created", 200


if __name__ == "__main__":
    app.run(debug=True, port=port, host = "0.0.0.0")
