# -- Program 2

# Write a program that computes the sum of the logarithms of all the primes from 2 to some number n, 
# and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities. 
# Test this for different values of n.

import math

n = 10000  # int(input('Enter an positive integer value:'))
count = 0
sum = 0

for i in range(2, n):
    # Reset for every iteration
    j = 2
    iter_div_count = 0

    while(j <= i/2):
        result = i

        if(i % j == 0):
            iter_div_count += 1
        j += 1

    if(iter_div_count == 0):
        sum = sum + math.log2(i)
        count += 1

print('Sum =', round(sum,2))
print('N = ', n)
print('Ratio = ', round(sum/n,2))
print('Total prime numbers between 1 and', n, 'is:', count)