Number1=float(input("enter first number "))
Number2=float(input("enter second number "))
Operation=input("enter operation (+,-,/,*) ")
if Operation=="+":
    print(Number1 , "+" , Number2,"= ",Number1+Number2)
elif Operation=="-":
    print(Number1 , "-" , Number2,"= ",Number1-Number2)
elif Operation=="*":
    print(Number1 , "*" , Number2,"= ",Number1*Number2)
elif Operation=="/":
    print(Number1 , "/" , Number2,"= ",Number1/Number2)