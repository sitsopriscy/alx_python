for number in range(100):
    if number < 99:
        print("{:02}, ".format(number), end="", flush=True)
    else:
        print("{:02}".format(number))

        