Temperature = input("Enter temperture")
Unit=list(Temperature.split(" "))
print(Unit)
if Unit[2]=="Celsius":
    print( Unit[0],"Celcius is equal to ", 1.8 * float(Unit[0]) + 32, "Fahrenheit")
    print( Unit[0],"Celcius is equal to ", (float(Unit[0]) + 273.15), "Kelvin")
elif Unit[2]=="Fahrenheit":
     print( Unit[0],"Fahrenheit  is equal to ", round((float(Unit[0])-32)*5/9,3), "Celcius")
     print(Unit[0], "Fahrenheit  is equal to ",  round(273.5 + (float((Unit[0])) - 32.0 * (5.0/9.0)),3), "Kelvin")
    
else:
    print( Unit[0],"Kelvin is equal to ", ( round(float(Unit[0]) - 273.15, 3)), "Celcius")
    print( Unit[0],"Kelvin is equal to ", ( round(9 / 5 * (float(Unit[0]) - 273.15) + 32, 3)), "Fahrenheit")
     

   