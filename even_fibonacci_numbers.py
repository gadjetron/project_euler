UPBOUND = 4000000

fibonacci_numbers = []

a, b = 1, 1 

while b < UPBOUND:
    a, b = b, a + b
    
    fibonacci_numbers.append(b)


even_fibonacci_numbers = [ 
    fib_number for fib_number in fibonacci_numbers 
        if fib_number % 2 == 0
]

print("Sum of even Fibonacci numbers (up to 4,000,000): {}".format(sum(even_fibonacci_numbers)))
