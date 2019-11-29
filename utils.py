import os

# Executa comando para limpeza do terminal de acordo com o S.O
def clear():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


def header():
    print('***********************************************')
    print('************ Caixa Eletrônico *****************')
    print('***********************************************')

def invalid_account():
    print('Numero de conta e/ou senha incorretos')