# Global vs Functional Scope


def fn(x):
    x += 1
    print('In fn(x), the value of x:', x)
    return x


x = 3
print('The value of x is:', x)
z = fn(x)
print('The value of x is:', x)
print('The value of z is:', z)
