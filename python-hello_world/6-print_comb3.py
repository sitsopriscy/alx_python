for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        if units_digit ==9 and tens_digit == 8:
             print("{:d}{:d}, ".format(tens_digit, units_digit), end="", flush=True)

        else:
            print("{:d}{:d}, ".format(tens_digit, units_digit), end="", flush=True)
    
            