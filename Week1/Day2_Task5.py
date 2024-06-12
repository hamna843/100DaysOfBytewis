str=input("Enter a tring for checking")
str = str.lower()
New_str = ""
for char in str:
    if char.isalpha():
        New_str+= char

if New_str == New_str[::-1]:
    print("IS A PALINDORM")

else:
    print("NOT A PALINDORM")