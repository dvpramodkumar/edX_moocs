# Factorial of a number using iteration


def factorial(n):
    i = 1
    result = 1

    if(n == 0):
        return result

    while(i <= n):
        result = result * i
        i += 1
    return result


print(factorial(6))
print(factorial(5))
print(factorial(1))
print(factorial(0))
