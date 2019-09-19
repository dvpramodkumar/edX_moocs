# String and Loops

s1 = "abcdefgh"

print('String is: ', s1)
print('String reversed is: ', s1[::-1])


# Code Sample

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
