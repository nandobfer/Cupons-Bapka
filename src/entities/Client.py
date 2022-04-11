import os
from util import *
from data.config import *

class Client():
    def __init__(self, id) -> None:
        self.id = id
        

    def login(self):
        try:
            self.data = readJSON(self.id)
            return True
        except:
            return False

    def printDados(self):
        os.system('cls')
        print("Dados do cliente:")
        for key in self.data:
            print(f'{key}: {self.data[key]}')


    def addCupom(self, quantity):
        self.cupons += quantity
