import requests
import json

def create_transaction(transaction):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://transactions-app-service:5001/create_transaction', data = json.dumps(transaction.to_dict()), headers=headers)
    return response.status_code == 200
