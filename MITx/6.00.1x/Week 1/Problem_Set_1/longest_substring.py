s = 'azcbobobegghakl'
sub_str = ''

# Variable used in Iteration

counter = 0
i = 0
begin = 0
end = 0

iter_substr = ''

print('Given String = ', s)
while(i < len(s) - 1):
    if(s[i] <= s[i+1]):
        #print(s[i], s[i+1])
        if(begin == 0):
            begin = i
        counter += 1
    else:
        iter_substr = s[begin:][:counter+1]

        # Check if current iteration substring larger than previous one
        if(len(iter_substr) > len(sub_str)):
            sub_str = iter_substr

        # Reset Iter Variable for Next Substring
        begin = 0
        counter = 0
    i += 1

print('Longest substring in alphabetical order is:', sub_str)