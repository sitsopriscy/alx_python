# import sys
# from sys import argv

# def print_arguments():
#     num_arguments = len(argv) - 1

#     if num_arguments == 0:
#         print("0 argument.")
#         print(":")
#     elif num_arguments == 1:
#         print("1 argument:")
#     else:
#         print("{} arguments:".format(num_arguments))

#     for i, arg in enumerate(sys.argv[1:], start=1):
#         print("{}: {}".format(i, arg))
     
        
# if __name__ == "__main__":
#     print_arguments()


#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1  # Subtract 1 to exclude the script name itself

    # Print the number of arguments
    print("{} argument{}{}".format(
        argv_len,
        's' if argv_len != 1 else '',
        '.' if argv_len == 0 else ':'
    ))

    # Print each argument with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
