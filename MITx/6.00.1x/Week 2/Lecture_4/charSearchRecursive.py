
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if(len(aStr) == 0):
        return False

    elif(len(aStr) == 1):
        if(aStr[0] == char):
            return True
        else:
            return False

    else:
        l = len(aStr)
        low = 0
        high = l - 1

        value = int((low + high) / 2)

        if(char < aStr[value]):
            return isIn(char, aStr[:value-1])

        elif(char > aStr[value]):
            return isIn(char, aStr[value+1:])
        else:
            return True


print(isIn('z', 'abcdefgh'))
print(isIn('x', 'egmmmorstvy'))
print(isIn('a', ''))
print(isIn('f', 'b'))
