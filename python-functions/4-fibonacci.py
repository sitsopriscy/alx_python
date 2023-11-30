def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]