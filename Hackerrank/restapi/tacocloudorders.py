import mathematics
import os
import random
import re
import sys


import requests
import json

def getTotalOrdersWrap() :
    urlhr = "https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=Barcelona"
    resphr = requests.get(urlhr)
    resulthr = json.loads(resphr.content)
    print(resulthr)

    url = "http://localhost:8080/api/tacoorders?recent"
    resp = requests.get(url)
    result = json.loads(resp.content)
    print(result)
    print(result['data'][0]['tacos'][0]['ingredients'][0]['type'])
    print(result['page'])
    print(result['total'])
    print("---------------")
    count = 0
    pages = result['page']
    for p in range(1,pages +1) :
        print(p)
    for i in result['data'][0]['tacos'][0]['ingredients']:
        if (i['type'] == 'WRAP') :
            count += 1
    return count

if __name__ == '__main__':
    print("Total WRAPS are: ", getTotalOrdersWrap())
