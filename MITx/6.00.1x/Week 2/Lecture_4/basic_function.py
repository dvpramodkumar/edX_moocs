def is_even(number=0):
    """ Checks if a given number is even or not """
    print('Number = ', number)
    return (number % 2 == 0)


print(is_even(19))


def square(x):
    return x * x


print(square(5)+2)


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b*x + c
