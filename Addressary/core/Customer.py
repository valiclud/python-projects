'''
Created on 29. 6. 2023

@author: valic
'''
from core.CustomerId import CustomerId

class Customer:

    def __init__(self, CustomerId, name, surname, address):
        self._CustomerId = CustomerId
        self._name = name
        self._surname = surname
        self._address = address
        
    def __str__(self):
        return f'Customer {self._CustomerId} + {self._name} + {self._surname}'