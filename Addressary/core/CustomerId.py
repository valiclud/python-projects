'''
Created on 29. 6. 2023

@author: valic
'''
class CustomerId:

    def __init__(self, customerId):
        self.customerId = customerId
        
    def __hash__(self):
        hash_value = hash(self.customerId) * 7
        return hash_value
    
    def __eq__(self, other):
        return isinstance(other, CustomerId) and self.customerId == other.customerId
    
    def __lt__(self, other):
        return self.customerId < other.customerId
    
    def __gt__(self, other):
        return self.customerId > other.customerId
    
    def __add__(self, other):
        return self.customerId + other.customerId
    
    def __str__(self):
        return str(self.customerId)
