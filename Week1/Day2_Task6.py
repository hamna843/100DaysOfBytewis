str1 = input("Enter first string")
str2 = input("Enter second string")
#list1 = [char for char in str1]
#list2 = [char for char in str2]
if(sorted(str1)==sorted(str2)):
    print("it is an Anagram")
else:
    print("it is not an Anagram")