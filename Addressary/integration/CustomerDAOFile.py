'''
Created on 30. 6. 2023

@author: valic
'''
import pickle

from integration.DAOInterface import DAOInterface
from core.CustomerId import CustomerId

class CustomerDAOFile(DAOInterface):

    def __init__(self):
        self._customers_data = [{}]
        for self._customers_data in pickle_loader('customers.plk'):
            pass

    def createCustomer(self, name, surname, address):
        newCustomerId = self.findLastCustomerId()
        dctr = {}   
        dctr['customerId'] = newCustomerId
        dctr['name'] = name
        dctr['surname'] = surname
        dctr['address'] = address
        self._customers_data.append(dctr)
    
    def findLastCustomerId(self):
        if all(len(d) == 0 for d in self._customers_data):
            return CustomerId(1)
        else:
            max_value = 0
            for l in self._customers_data:
                for key in l:
                    if (key == 'customerId') :
                        if l[key] > max_value:
                            max_value = l[key]
            return CustomerId(max_value) + CustomerId(1)
    
    def deleteCustomer(self, customerId):
        for l in self._customers_data :
            for key in l:
                if (key == 'customerId') :
                    if CustomerId(l[key]) == CustomerId(int(customerId)):
                        self._customers_data.remove(l)
        
    def updateCustomer(self, idCustomer, name, surname, address):
        customer = self.findByCustomerId(int(idCustomer))
        dctr = {}   
        dctr['customerId'] = int(idCustomer)
        dctr['name'] = name
        dctr['surname'] = surname
        dctr['address'] = address
        self._customers_data.remove(customer)
        self._customers_data.append(dctr)

    def findByCustomerId(self, customerId):
        if all(len(d) == 0 for d in self._customers_data):
            return None
        else:
            for l in self._customers_data:
                for key in l:
                    if (key == 'customerId') :
                        if l[key] == customerId:
                            return l
            return None

    def pickle_dump(self, filename, data):
        with open(filename, 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    def getAllCustomers(self):
        return self._customers_data
    
    def close(self):
        self._CustomerDAOFile.pickle_dump('customers.plk', self._CustomerDAOFile._customers_data)

def pickle_loader(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break
            
