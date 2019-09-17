# Number guessing using Bisection Search

print('Please think of a number between 1 and 100')

low = 0
high = 100
answer = 0
choice = None

while(True):
    answer = int((low + high)/2)
    print('Is your secret number ', answer)
    choice = str.lower(input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. \
    Enter \'c\' to indicate I guessed correctly'))

    if(choice == 'l'):
        low = answer
        answer = int((low + high)/2)

    elif(choice == 'h'):
        high = answer
        answer = int((low + high)/2)
    elif(choice == 'c'):
        break
    else:
        print('Sorry, I did not understand your input')
print('Game over', end =' ')
print('Your secret number is ', answer)        
