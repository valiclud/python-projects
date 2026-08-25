'''
Created on 24. 5. 2024

@author: valic
'''

numbers = {0:"", 1:" One", 2:" Two", 3:" Three", 4:" Four", 5:" Five", 6:" Six", 7:" Seven", 8:" Eight", 9:" Nine", 
               10: " Ten", 11:" Eleven", 12:" Twelve", 13:" Thirteen", 14:" Fourteen", 15:" Fifteen", 16:" Sixteen", 17:" Seventeen",
              18:" Eighteen", 19:" Nineteen", 20: " Twenty", 30:" Thirty", 40: " Forty", 50: " Fifty", 60: " Sixty", 70:" Seventy", 80:" Eighty", 90:" Ninety"}
hundred = " Hundred"
thousand = " Thousand"
million = " Million"
billion = " Billion"

def getWords(number):
    result = ""
    if number >= 1000000000:
        n= number // 1000000000
        result = getHundreds(n) + billion
        number = number % 1000000000
    if number >= 1000000:
        n= number // 1000000
        result = result + getHundreds(n) + million
        number = number % 1000000            
    if number >= 1000:
        n= number // 1000
        result = result + getHundreds(n) + thousand
        number = number % 1000
    result = result + getHundreds(number)      

    return result.strip()

def getHundreds(number):
    result = ""
    if number >= 100:
        n = number // 100
        result = result + numbers[n] + hundred
        number = number % 100
    if number >= 20:
        n = number // 10
        result = result + numbers[n*10]
        number = number % 10
    if number < 20:
        result = result + numbers[number]            
    return result        

if __name__ == '__main__':
    n = int(input()) + 1
    result = 0
    for x in range(n):
        word = getWords(x).replace(" ", "")
        if (x<100 or x%100 == 0):
            result += len(word)
        else:
            result += len(word)+3
    print(result)    
    