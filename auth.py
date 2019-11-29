from database import connect
from getpass import getpass


class Auth:

    @staticmethod
    def auth_client():
        account_number = input('Digite o numero da sua conta: ')
        password = getpass('Digite sua senha: ')
        db = connect()
        user = db.accounts.find_one({
                    'number': account_number,
                    'pass': password
                })
        return user if user else False
        