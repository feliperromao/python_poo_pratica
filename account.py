from database import connect

class Account:

    def __init__(self, account_data):
        self._id = account_data._id
        self.number = account_data.number
        self.balance = account_data.balance
        self.name = account_data.name
        self.admin = account_data.admin


    # Executa o saque da conta
    def withdraw(self, value):
        if self.balance - value < 0:
            print("Impossivel realizar saque, Saldo insuficiente.")
            return False
        else:
            balance = self.balance - value
            self.set_balance(balance)


    # Executa o depósito na conta
    def deposit(self):
        pass


    # Executa a transferencia de um valor entre contas
    def transfer(self):
        pass

    
    def set_balance(self, value):
        self.balance = value
        #TODO Atualizar documento no banco de dados
        db = connect()
        db.accounts.update_one({'_id': self._id}, {'balance': self.balance
        })
