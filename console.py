class CashMachineConsole:

    @staticmethod
    def call_operation(account):
        option_typed = CashMachineConsole.get_menu_options_typed()
        CashMachineOperation.do_operation(option_typed, account)
        

    @staticmethod
    def get_menu_options_typed():

        for option in CashMachineOperation.OPERATIONS:
            print(f'{option["option"]} - {option["name"]}')

        return input('Selecione uma das opções acima: ')


class CashMachineOperation:

    OPERATIONS = [
        {
            'option': '1',
            'name': 'Saldo',
            'operation': 'show_ballance_operation'
        },
        {
            'option': '2',
            'name': 'Saque',
            'operation': 'withdraw_operation'
        },
        {
            'option': '3',
            'name': 'Deposito',
            'operation': 'deposit_operation'
        }
    ]
    
    @staticmethod
    def do_operation(selected, data):
        for option in CashMachineOperation.OPERATIONS:
            if option['option'] == selected:
                operation = getattr(CashMachineOperation, option['operation'])
                operation(data)

    
    @staticmethod
    def show_ballance_operation(data):
        print('Mostrando saldo')


    @staticmethod
    def withdraw_operation(data):
        print('Realizando saque')


    @staticmethod
    def deposit_operation(data):
        print('Realizando deposito')