'''
Created on 21. 8. 2023

@author: valic
'''
from core.FlightRocketId import FlightRocketId

class Flight:

    def __init__(self, FlightRocketId, speed, distance, height, createdAt):
        self._FlightRocketId = FlightRocketId
        self._speed = speed
        self._distance = distance
        self._height = height
        self._createdAt = createdAt
    
    def __str__(self):
        return f'Flight {self._FlightRocketId} + {self._speed} + {self._distance}'
