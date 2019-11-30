from database import connect

class Account:

    OPERATIONS = [
        {
            'option': '1',
            'name': 'Saldo',
            'operation': 'show_ballance_operation',
            'need_is_admin': False
        },
        {
            'option': '2',
            'name': 'Saque',
            'operation': 'withdraw_operation',
            'need_is_admin': False
        },
        {
            'option': '3',
            'name': 'Deposito',
            'operation': 'deposit_operation',
            'need_is_admin': False
        },
        {
            'option': '4',
            'name': 'Adicionar notas',
            'operation': 'add_bills',
            'need_is_admin': True
        }
    ]

    def __init__(self, account_data):
        self._id = account_data['_id']
        self.number = account_data['number']
        self.balance = account_data['balance']
        self.name = account_data['name']
        self.admin = account_data['admin']


    def show_ballance_operation(self):
        print(f'Saldo em conta é de: {self.balance}')


    # Executa o saque da conta
    def withdraw_operation(self, value):
        if self.balance - value < 0:
            print("Impossivel realizar saque, Saldo insuficiente.")
            return False
        else:
            balance = self.balance - value
            self.set_balance(balance)


    # Executa o depósito na conta
    def deposit_operation(self):
        pass


    # Executa a transferencia de um valor entre contas
    def transfer(self):
        pass

    
    def set_balance(self, value):
        self.balance = value
        #TODO Atualizar documento no banco de dados
        db = connect()
        db.accounts.update_one({'_id': self._id}, {'balance': self.balance})


    def show_operations(self):
        for option in Account.OPERATIONS:
            operation_string = f'{option["option"]} - {option["name"]}'
            
            if option['need_is_admin'] and self.admin or not option['need_is_admin']:
                print(operation_string)

        return input('Selecione uma das opções acima: ')

    
    def call_operation(self, selected):
        for option in Account.OPERATIONS:
            if option['option'] == selected:
                operation = getattr(self, option['operation'])
                operation()