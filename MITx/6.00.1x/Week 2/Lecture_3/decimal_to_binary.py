x = 19
result = ''
number = x

if(x == 0):
    result = '0'
else:
    while(x > 0):
        result = str(x % 2) + result
        x = x//2

print('Decimal = ', number)
print('Binary = ', result)
