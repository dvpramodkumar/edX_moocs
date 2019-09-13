# string = input('Enter a string: ')
# print('You have entered ', string)

string = 'aeio'

str_vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for ch in string:
    if(ch in str_vowels):
        cnt += 1

print('Number of vowels: ', cnt)
