

def wrapper(f):
    def fun(l):
        for index, s in enumerate(l):
            if (s[0:2] == "91" and len(s) > 10):
                l[index] = "+" + s[0:2] + " " + s[2:7] +" "+ s [7:12]
            elif (s[0] == "+"):
                l[index] = s[0:3] + " " + str(int(s[3:8])) +" "+ str(s[8:13])
            elif (s[0] == "0"):
                s.strip("0")
                l[index] = "+91 " + str(int(s[0:6])) +" "+ str(s[6:11])
            else :
                l[index] = "+91 " + str(int(s[0:5])) +" "+ str(s[5:10])
        l.sort()
        f(l)
    return fun 

@wrapper        #DODELAT
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
    