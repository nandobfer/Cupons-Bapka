from entities.Client import *
from data.config import *
import os

os.system('cls')
id = requestClientId()
client = Client(id)
if client.login():
    client.printDados()
    choose = requestCupomHandler()
    if choose == ADD_CUPOM:
        client.addCupom(N_CUPONS)
    else:
        client.removerCupom(N_CUPONS)
else:
    choose = requestSignUp()
    if choose == SIGNUP:
        client.cadastrar()
    else:
        os.system('cls')