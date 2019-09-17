# Prints the nth Prime Number

n = 1000  # int(input('Enter an positive integer value:'))
count = 0

for i in range(2, 10000):
    # Reset for every iteration
    j = 2
    iter_div_count = 0

    while(j <= i/2):
        if(i % j == 0):
            iter_div_count += 1
        j += 1

    if(iter_div_count == 0):
        count += 1

    if(count == n):
        print('The', n,'th Prime number is:', i)
        break
