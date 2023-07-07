'''
Created on 29. 6. 2023

@author: valic
'''
#from abc import ABC, abstractmethod
import abc
from core.CustomerId import CustomerId

class DAOInterface(abc.ABC):

    @abc.abstractmethod
    def createCustomer(self, name, surname, address, commentary):
        pass
    
    @abc.abstractmethod
    def updateCustomer(self, CustomerId, name, surname, address, commentary):
        pass

    @abc.abstractmethod
    def deleteCustomer(self, CustomerId):
        pass