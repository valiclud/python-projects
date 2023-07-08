'''
Created on 29. 6. 2023

@author: valic
'''
#from abc import ABC, abstractmethod
import abc

class DAOInterface(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def createCustomer(self, name, surname, address, commentary):
        pass
    
    @abc.abstractmethod
    def updateCustomer(self, CustomerId, name, surname, address, commentary):
        pass

    @abc.abstractmethod
    def deleteCustomer(self, CustomerId):
        pass
    
    @abc.abstractmethod
    def getAllCustomers(self):
        pass
    
    @abc.abstractmethod
    def findByCustomerId(self, customerId):
        pass
    
    @abc.abstractmethod
    def close(self):
        pass
    