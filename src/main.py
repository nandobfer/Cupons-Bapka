from entities.Client import *
import os

os.system('cls')
id = int(input('Digite o ID de cliente: '))
client = Client(id)
if client.login():
    client.printDados()
else:
    print("Cliente não cadastrado")