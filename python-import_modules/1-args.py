import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1 

    if num_arguments == 0:
        print("0 argument.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()

    print("[stderr]: [Anything]")
    
