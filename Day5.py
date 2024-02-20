# Day 5
# Writing a Program to print the first 10 numbers of the Fibonacci sequence

def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]

def main():
    # Getting the first 10 numbers of the Fibonacci sequence
    fibonacci_numbers = fibonacci_sequence(10)

    # Printing the the result
    print("First 10 numbers of the Fibonacci sequence:", fibonacci_numbers)

if __name__ == "__main__":
    main()
    
