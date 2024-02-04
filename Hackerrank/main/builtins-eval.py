def fun_generator():
	yield "Hello world!!"
	yield "Geeksforgeeks"


if __name__ == '__main__':
    #s = input()
    #eval(s)
    obj = fun_generator()
    print(obj)
    print(next(obj))
    print(next(obj))



