# Requests definitions
def requestClientId():
    return int(input('Digite o ID de cliente: '))
def requestCupomHandler():
    return input('Deseja adicionar ou remover cupons? (+/-): ')
ADD_CUPOM = '+'
REMOVE_CUPOM = '-'
def requestSignUp():
    return input("Cliente não cadastrado, deseja se cadastrar? (s/n): ")
SIGNUP = 's'

# Database definitions


# quantidade de cupons
N_CUPONS = 1

# clients data file
CLIENTS_DATA = 'data/clients.json'

# data constants
CUPONS = "Cupons"
NOME = "Nome"
CPF = "CPF"
EMAIL = "E-mail"