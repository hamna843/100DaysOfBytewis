factorial=1
def FactorialCalculator(Num):
    if(Num>1):
        return(Num*FactorialCalculator(Num-1))
    else:
        return 1

Num=int(input("Enter number"))
print("Factorial of ", Num, "is " ,FactorialCalculator(Num))
