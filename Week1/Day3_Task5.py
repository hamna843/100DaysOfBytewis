
# print(str[0::1])
# print(str[1::])
def palindromCheck(str):
    
    if not str:
        return ""

    max_length = 0
    palindrome = ""

    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                palindrome = substring

    return palindrome
str=input("enter the string ")
print(palindromCheck(str))