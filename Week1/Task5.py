Number1=int(input("enter first number "))
Number2=int(input("enter second number "))
Number3=int(input("enter first number "))
if Number1>Number2 & Number1>Number3:
    print(Number1, " is greatest")
elif Number2>Number1 & Number1>Number3:
    print(Number2, " is greatest")

else:
    print(Number3, " is greatest")