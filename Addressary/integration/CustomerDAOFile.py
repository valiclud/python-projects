'''
Created on 30. 6. 2023

@author: valic
'''
import pickle
from pathlib import Path

from integration.DAOInterface import DAOInterface
from core.CustomerId import CustomerId

class CustomerDAOFile(DAOInterface):

    def __init__(self):
        self._customers_data = []
        self.script_location = Path(__file__).absolute().parent
        self.file_location = self.script_location / 'customers.plk'
        for self._customers_data in pickle_loader(self.file_location):
            pass

    def createCustomer(self, name, surname, address):
        newCustomerId = self.findLastCustomerId()
        if(newCustomerId == None):
            newCustomerId = CustomerId(0)
        dctr = {}   
        dctr['customerId'] = CustomerId(newCustomerId + CustomerId(1))
        dctr['name'] = name
        dctr['surname'] = surname
        dctr['address'] = address
        self._customers_data.append(dctr)
    
    def findLastCustomerId(self):
        if (len(self._customers_data) == 0):
            return None
        else:
            max_value = CustomerId(1)
            for l in self._customers_data:
                for key in l:
                    if (key == 'customerId') :
                        if l[key] > max_value:
                            max_value = l[key]
            
            return max_value
    
    def deleteCustomer(self, customerId):
        for l in self._customers_data :
            for key in l:
                if (key == 'customerId') :
                    if l[key].customerId == customerId:
                        self._customers_data.remove(l)
        
    def updateCustomer(self, idCustomer, name, surname, address):
        customer = self.findByCustomerId(idCustomer)
        dctr = {}   
        dctr['customerId'] = customer.get('customerId')
        dctr['name'] = name
        dctr['surname'] = surname
        dctr['address'] = address
        self._customers_data.remove(customer)
        self._customers_data.append(dctr)

    def findByCustomerId(self, customerId):
        if (len(self._customers_data) == 0):
            return None
        else:
            for l in self._customers_data:
                for key in l:
                    if (key == 'customerId') :
                        if l[key] == CustomerId(customerId):
                            return l
            return None

    def pickle_dump(self, filename, data):
        with open(filename, 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    def getAllCustomers(self):
        return self._customers_data
    
    def close(self):
        self.pickle_dump(self.file_location, self._customers_data)

def pickle_loader(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break
            
