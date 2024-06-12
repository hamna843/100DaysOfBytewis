import random
num = random.randint(1, 100)
UserNumber= int(input("Enter a number"))
while(UserNumber!=num):
    if UserNumber<num:
        print("YOUR GUESS IS TOO LOW")
    else:
        print("YOUR GUESS IS TOO HIGH")
    UserNumber= int(input("Enter again"))
print("YOU GUESSED IT RIGHT!!!!")
