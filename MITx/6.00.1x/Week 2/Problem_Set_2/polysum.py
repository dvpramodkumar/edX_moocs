# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of
# the regular polygon.
# The function returns the sum, rounded to 4 decimal places

from math import *


def polysum(n, s):
    numerator = (0.25 * n * s ** 2)
    denominator = (tan(pi/n))
    area = (numerator/denominator)
    perimeter = n * s
    total_sum = area + perimeter ** 2
    return round(total_sum, 4)
