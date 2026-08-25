'''
Created on 4. 11. 2023

@author: valic
'''

import requests
import json

def getNumDraws(year):
    count = 0
    for goal in range(0,8):
        url = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={2}&page=1".format(str(year), str(goal), str(goal))
        rsp = requests.get(url)
        json = rsp.json()
        count += json['total']
    return count

def getTotalPages(competition, year, winner, team):
    url = "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&{2}={3}&page=1".format(competition, year,team, winner)
    rsp = requests.get(url)
    js = rsp.json()
    total_pages = js['total_pages']
    return total_pages

def getWinnerTotalGoals(competition, year):
    total_goals = 0
    url =  "https://jsonmock.hackerrank.com/api/football_competitions?name={0}&year={1}".format(competition,year)
    rsp = requests.get(url)
    js = rsp.json()
    winner = js['data'][0]['winner']
    total_pages1 = getTotalPages(competition, year, winner, 'team1')
    for p in range(1, total_pages1 + 1) :
        url2 = "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team1={2}&page={3}".format(competition, year, winner, p)
        rsp2 = requests.get(url2)
        js2 = rsp2.json()
        for d in js2['data']:
            total_goals += int(d['team1goals'])
            
    total_pages2 = getTotalPages(competition, year, winner, 'team2')
    for p in range(1, total_pages2 + 1) :
        url3 = "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team2={2}&page={3}".format(competition, year, winner, p)
        rsp3 = requests.get(url3)
        js3 = rsp3.json()
        for d in js3['data']:
            total_goals += int(d['team2goals'])
    return total_goals
                
if __name__ == '__main__':
    #print(getNumDraws(2011))
    print(getWinnerTotalGoals("UEFA Champions League", 2011))