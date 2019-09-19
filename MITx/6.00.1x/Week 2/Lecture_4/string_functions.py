# This program explores all the built-in string functions in Python


def f(val):
    print(val)


s = 'abc'
f(s.capitalize)
f(s.capitalize())

str1 = 'exterminate!'
str2 = 'number one - the larch'

f(str1.upper)
f(str2.swapcase())
f(str1.index('e'))
f(str1.find('f'))
str1 = str1.replace('e', '*')
f(str1)
f(str2.replace('one', 'seven'))
