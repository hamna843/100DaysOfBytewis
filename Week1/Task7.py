Str = input('Enter the string ')
count = 0

String = Str.lower()
for vowel in Str:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count+=1

print('Total vowels are :' + str(count))