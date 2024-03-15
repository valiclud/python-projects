'''
Created on 10. 8. 2023

@author: valic
'''

def handshake(n):
    if n == 1:
        c = 0
    if n == 2:
        c = 1
    a = 1
    for h in range(2, n):
        c = a + h 
        a = c
    return(c)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    
    for t_itr in range(t):
        n = int(input().strip())

            
        result = handshake(n)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
