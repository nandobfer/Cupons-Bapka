import json
import sys, os
sys.path.append(os.path.dirname("data"))
from data.config import *

def readJSON():
        with open(CLIENTS_DATA, "r") as read_file:
                data = json.load(read_file)
        return data
