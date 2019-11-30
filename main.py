from utils import clear, header, invalid_account
from console import CashMachineConsole
from auth import Auth
from account import Account

def main():
    clear()
    header()

    account_auth = False

    while not account_auth:
        account_auth = Auth.auth_client()
        if not account_auth:
            clear()
            header()
            invalid_account()

    account = Account(account_auth)

    option = account.show_operations()
    account.call_operation(option)

if __name__ == '__main__':
    while True:
        main()
        input('Pressione <ENTER> para continuar... ')