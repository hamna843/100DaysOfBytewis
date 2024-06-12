str = input("Enter string")
print(list(str.split(" "))[::-1])
RevStr=""
for word in list(str.split(" "))[::-1]:
    RevStr=RevStr+word+" "
print(RevStr)