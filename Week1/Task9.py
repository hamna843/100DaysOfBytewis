word=input("enter word to check for palindrom ")
if word == word[::-1]:
    print("it is a palindrom")
else:
    print("not a palindrom")