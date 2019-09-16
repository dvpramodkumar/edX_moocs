s = 'azcbobobegghakl'
sub_str = 'bob'

i = 0
n = 3
cnt = 0

while(i < len(s)):
    if(s[i:][:n] == sub_str):
        cnt += 1
    i +=1
print('Number of times ', sub_str, ' occurs is: ', cnt)
