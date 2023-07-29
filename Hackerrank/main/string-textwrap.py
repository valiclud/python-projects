import textwrap

def wrap(string, max_width):
    #print(textwrap.wrap(string,max_width)) #return list
    #print(textwrap.fill(string,max_width)) #return string
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)