n_terms = int(input ("eneter number of terms "))  
  

N1 = 0  
N2 = 1  
count = 0  
  
if n_terms <= 0:  
    print ("enter a positive integer")  

elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ", N1)  

else:  
    print ("The fibonacci sequence  is:")  
    while count < n_terms:  
        print(N1)  
        nth = N1 + N2   
        N1 = N2  
        N2 = nth  
        count += 1  