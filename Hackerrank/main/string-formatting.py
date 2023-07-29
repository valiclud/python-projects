def print_formatted(number):
    output_string = ""
    for i in range(number):
        octal = oct(i)
        hexa = hex(i).capitalize()
        binary = bin(i)
        output_string += "{0}  {1}  {2}  {3}\n".format(i, octal, hexa, binary)
    print(output_string)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)