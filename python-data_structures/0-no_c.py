#!/usr/bin/python3

def no_c(my_string):
    result = ''.join(char for char in my_string if char not in 'cC')
    return result

if __name__ == "__main__":
   
    input_string = "Holberton School"
    output_string = no_c(input_string)
    print(output_string)
