def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if(a == b):
        return a
    elif(b == 0):
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(2, 2))
print(gcdRecur(2, 3))
print(gcdRecur(30, 3))
print(gcdRecur(24, 12))
