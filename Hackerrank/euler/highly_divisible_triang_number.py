def noOfDivisors(n) :
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0) :
            if (n / i == i) :
                cnt = cnt + 1
            else : 
                cnt = cnt + 2                
    return cnt
        
def getDict(t, triangles):
    result = {}
    r = noOfDivisors(t)       
    #if r not in triangles.values() :
    result.update({t:r})
    return result
    #return {}
        
def getTriangles():
    triangles = {}
    for y in range (1, 42000):
        t = int(y * (y+1) / 2)
        d = getDict(t, triangles)
        triangles.update(d)
    return triangles

if __name__ == '__main__':
    triangles = getTriangles()
    print (triangles)
    #print(max(triangles.values()))
    n = int(input())
    for _ in range(n):
        i = int(input())
        for x, y in triangles.items():
            if y > i:
                print(x)
                break
