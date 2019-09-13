varA = 1
varB = 'text'

if(isinstance(varA,str) or isinstance(varB,str)):
    print('string involved')
elif (varA > varB):
    print('bigger')
elif (varA == varB):
    print('equal')
else:
    print('smaller')

for i in range(1,11):
    if(i % 2 == 0):
        print(i)
print('Goodbye!')

i = 2
while(i <= 10):
    print(i)
    i += 2
print('Goodbye!')

i = 10
while(i >= 2):
    if(i == 10):
        print('Hello!')
    print(i)
    i -= 2

end = 6

i = 1
count = 0
while(i <= end):
    count += i
    i += 1
print(count)


for i in range(10,1,-2):
    if(i == 10):
        print('Hello!')
    print(i)


end = 6
count = 0
for i in range(1, end + 1):
    count += i
    i += 1
print(count)    