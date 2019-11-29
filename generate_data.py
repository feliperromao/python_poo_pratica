from database import connect

accounts = [
    {
        "number": "000",
        "pass": "000",
        "balance": 0,
        "name": "Administrador",
        "admin": True
    },
    {
        "number": "1234",
        "pass": "1234",
        "balance": 12500,
        "name": "Felipe Romao",
        "admin": False
    },
    {
        "number": "456",
        "pass": "456",
        "balance": 5900,
        "name": "Pereira Da Silva",
        "admin": False
    }
]

bills = [
    {
        "bill": "10",
        "ammount": 50
    },
    {
        "bill": "20",
        "ammount": 50
    },
    {
        "bill": "50",
        "ammount": 50
    },
    {
        "bill": "100",
        "ammount": 50
    },
]


db = connect()

db.accounts.insert_many(accounts)
db.bills.insert_many(bills)