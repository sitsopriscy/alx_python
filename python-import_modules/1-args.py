import sys

def print_arguments():
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1  # Exclude the script name itself

    # Print the number of arguments
    if num_arguments == 0:
        print("0 argument.")
        print(".")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
     
        
if __name__ == "__main__":
    print_arguments()
