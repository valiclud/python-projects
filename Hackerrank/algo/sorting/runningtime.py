'''
Created on 3. 8. 2023

@author: valic
'''

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        e = arr[i]
        if e < arr[0]:
            j = i
            for num in range(j, 0, -1) :
                arr[j] = arr[j-1]
                j-=1
                count +=1
            arr[0] = e  
        else :
            j = i-1
            while j >= 0 and e < arr[j]:  
                arr[j+1] = arr[j]  
                j -= 1
                count +=1
            arr[j+1] = e  
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()