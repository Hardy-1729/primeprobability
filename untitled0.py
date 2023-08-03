import math
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False


    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def prob(a,b):
    l=[]
   
 
    for i in range(a,b+1):
       if is_prime(i) is True:
           l+=[i]
    return (len(l))/math.gcd(len(l), b-a+1), (b-a+1)/ math.gcd(len(l), b-a+1)

n=int(input("Enter range: "))

n1=int(input("Enter numerator: "))
d=int(input("Enter denominator: "))

for i in range(1,n+1):
    t=[]
    
    k,k1=prob(0,i)    
    
    if k==n1 and k1==d:
        t+=[i]
        print(t)
    