'''
Created on 21. 8. 2023

@author: valic
'''
from core.FlightRocketId import FlightRocketId

class Rocket:

    def __init__(self, FlightRocketId,  name, sort, speedMax,
                  heightMax, distanceMax, createdAt):
        self._FlightRocketId = FlightRocketId
        self._name = name
        self._sort = sort
        self._speedMax = speedMax
        self._heightMax = heightMax
        self._distanceMax = distanceMax
        self._createdAt = createdAt
        
    def __str__(self):
        return f'Rocket {self._FlightRocketId} + {self._name} + {self._sort}'      