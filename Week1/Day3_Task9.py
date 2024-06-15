string1="kitten"
string2="sitting"
subsitution=0
deletion=0
insertion=0
if len(string1)==len(string2):
    for charIndex in range(len(string2)):
        if string1[charIndex]!=string2[charIndex]:
            subsitution+=1
elif len(string1)>len(string2):
    deletion=deletion+1
    for charIndex in range(len(string2)):
        if string1[charIndex]!=string2[charIndex]:
            subsitution+=1
else:
    insertion=insertion+1
    for charIndex in range(len(string1)):
        if string1[charIndex]!=string2[charIndex]:
            subsitution+=1

print(insertion+deletion+subsitution)