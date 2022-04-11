from entities.Client import *
from data.config import *
import os

os.system('cls')
id = int(input('Digite o ID de cliente: '))
client = Client(id)
if client.login():
    client.printDados()
    choose = input('Deseja adicionar ou remover cupons? (+/-): ')
    if choose == '+':
        client.addCupom(N_CUPONS)
    else:
        client.removerCupom(N_CUPONS)
else:
    print("Cliente não cadastrado, deseja se cadastrar? (s/n): ")
    if input() == 's':
        client.cadastrar()
    else:
        pass