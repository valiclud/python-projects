'''
Created on 29. 6. 2023

@author: valic
'''
class CustomerId:

    def __init__(self, customerId):
        self._customerId = customerId
        
    def __hash__(self):
        hash_value = hash(self._customerId) * 7
        print(f'Calling hash for {self._customerId}: {hash_value}')
        return hash_value
    
    def __eq__(self, other):
        return isinstance(other, CustomerId) and self._customerId == other._customerId
    
    def __lt__(self, other):
        return self._customerId < other._customerId
    
    def __gt__(self, other):
        return self._customerId > other._customerId
    
    def __add__(self, other):
        return self._customerId + other._customerId
    
    def __str__(self):
        return f'Id {self._customerId}'
