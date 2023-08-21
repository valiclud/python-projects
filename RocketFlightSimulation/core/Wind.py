'''
Created on 21. 8. 2023

@author: valic
'''

from core.FlightRocketId import FlightRocketId

class Wind:

    def __init__(self, FlightRocketId, windDirectionName, windSpeed):
        self._FlightRocketId = FlightRocketId
        self._windDirectionName = windDirectionName
        self._windSpeed = windSpeed
      
    def __str__(self):
        return f'Wind {self._FlightRocketId} + {self._windDirectionName} + {self._windSpeed}'