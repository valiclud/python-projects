'''
Created on 21. 8. 2023

@author: valic
'''

class FlightRocketId:

    def __init__(self, flightRocketId):
        self._flightRocketId = flightRocketId
  
    def __hash__(self):
        hash_value = hash(self._flightRocketId) * 7
        return hash_value
    
    def __eq__(self, other):
        return isinstance(other, other._flightRocketId) and self._flightRocketId == other._flightRocketId
    
    def __lt__(self, other):
        return self._flightRocketId < other._flightRocketId
    
    def __gt__(self, other):
        return self._flightRocketId > other._flightRocketId
    
    def __add__(self, other):
        return self._flightRocketId + other._flightRocketId

        
    def __str__(self):
        return str(self._flightRocketId)
        