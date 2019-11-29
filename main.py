from utils import clear, header, invalid_account
from console import CashMachineConsole
from auth import Auth

def main():
    clear()
    header()

    account = False

    while not account:
        account = Auth.auth_client()
        if not account:
            clear()
            header()
            invalid_account()

    CashMachineConsole.call_operation(account)


if __name__ == '__main__':
    while True:
        main()
        input('Pressione <ENTER> para continuar... ')