# Computer the 4th power of a number


def square(x):
    return x * x


def fourthPower(x):
    return square(x) * square(x)


# Using iteration

print(square(5) + 2)
print(fourthPower(2))


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    if(exp == 0):
        return 1

    else:
        i = 0
        result = 1

        while(exp > 0):
            result *= base
            exp -= 1

        return result


print(iterPower(2, 10))
print(iterPower(2, 5))
