def factorial_iterative(n):
    if n < 0:
        return "Factorial doesn't exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


num = 7
print(f"The factorial of {num} is {factorial_iterative(num)}") 