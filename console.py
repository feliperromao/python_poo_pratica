class CashMachineConsole:

    @staticmethod
    def get_menu_options_typed():
        print('1 - Saldo')
        print('2 - Saque')
        return input('Selecione uma das opções acima: ')

    @staticmethod
    def call_operation():
        return CashMachineConsole.get_menu_options_typed()
        

class CashMachineOperation:
    pass