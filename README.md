
Description: 
Background:
  This is a simple backend application consisting of two services: accounts and transactions. 
  The accounts service exposes two API:s, one that accepts the user information (customerID, initialCredit)
  and opens a new “current account” of already existing customers, and another that shows the user info Name, Surname, balance,
  and transactions of the accounts
  The criteria of the accounts service is to opena an account connected to the user whose ID is customerID, and sends a transaction to
  the new account if the initialCredit is not 0.
  
  The transactions service is only aimed to create a tansaction when called and outputs the transaction data to the console.

Setup:
  The services run on docker containers that can be run and interact with eachother within the same docker network. 
  The data used to test the services are saved in memory as dummy_data, i.e no database connections used
  

How to run: 
  Run both of the services seperately following the same following procedures. 
  Create a virtual environment using ```python3 -m venv .venv``` and activate ```source .venv/bin/activate```
  In both of the services, and an .env file with PORT=<your_port>.
  Run 
  ```
    make install
    make deploy
    make run
  ```
  to run the docker app. Make sure to have the docker deamon running in the background.

Test senarios:
  Goto http://127.0.0.1:5000/new_account/1/0 to create an account with no transaction for user with ID 1.
  View the user data you modified by fetching http://127.0.0.1:5000/user_info/1

  Goto http://127.0.0.1:5000/new_account/1/3 to create a transaction with amount 3 and fetch the user data 
  to see all the accounts and their transactions for the user, and the updated balance.

Example user data:
```
[
    {
        "user_id": 0,
        "Name": "Dan",
        "Surname": "Johnson",
        "balance": 3,
        "accounts": [
            {
                "id": "6YN7",
                "transactions": [
                    {
                        "id": "B3AG",
                        "amount": 1
                    }
                ]
            },
            {
                "id": "269D",
                "transactions": []
            },
            {
                "id": "0AIF",
                "transactions": [
                    {
                        "id": "EAMY",
                        "amount": 1
                    }
                ]
            },
            {
                "id": "6C3J",
                "transactions": [
                    {
                        "id": "4510",
                        "amount": 1
                    }
                ]
            },
            {
                "id": "GX3Y",
                "transactions": []
            },
            {
                "id": "ZZDB",
                "transactions": [
                    {
                        "id": "CIYH",
                        "amount": -1
                    }
                ]
            },
            {
                "id": "79J1",
                "transactions": [
                    {
                        "id": "139X",
                        "amount": 1
                    }
                ]
            }
        ]
    },
    {
        "user_id": 1,
        "Name": "Maria",
        "Surname": "Johnson",
        "balance": 0,
        "accounts": [
            {
                "id": "GGBY",
                "tansactions": []
            },
            {
                "id": "FBGC",
                "transactions": []
            }
        ]
    },
    {
        "user_id": 3,
        "Name": "Sofi",
        "Surname": "Johnson",
        "balance": 0,
        "accounts": [
            {
                "id": 1,
                "tansactions": []
            }
        ]
    }
]
```

Improvement suggestions:
  Create tests using pytest
  Use docker compose
  Add additional API:s
  Add logging  
