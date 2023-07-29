import numpy

def arrays(arr):
    a = numpy.array(arr,float)
    return numpy.flip(a)
    

if __name__ == '__main__':
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)