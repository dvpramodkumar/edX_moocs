def iterative_GCD(a, b):
    min = 0

    if(a <= 0 or b <= 0):
        print('Input must be positive and non-zero')
        return

    if(a < b):
        min = a
    elif(a > b):
        min = b
    else:
        return a

    i = min
    while(i >= 1):
        if(b % i != 0 or a % i != 0):
            i -= 1
        else:
            break
    return i


print('GCD = ', iterative_GCD(2, 2))
print('GCD = ', iterative_GCD(2, 3))
print('GCD = ', iterative_GCD(2, 12))
print('GCD = ', iterative_GCD(3, 6))
print('GCD = ', iterative_GCD(6, 12))
print('GCD = ', iterative_GCD(2, 0))
