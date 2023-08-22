import math
while True:
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
        
        for i in range (a,b+1):
            if is_prime(i) is True:
                l+=[i]
        return (len(l)),(b-a+1)
    
    def ll(n):
        for i in range(1,n):
            if 2**i>n:
                return (i-1),2**(i-1)+1
                break
    
    def diff(n):
        a,b=ll(n)
        c,d=prob(0,n)
        
        return (-1*(a*d-c*b)/math.gcd((a*d-c*b),(d*b))),((d*b)/math.gcd((a*d-c*b),(d*b)))
    
    k=int(input("Enter range: "))
    
    for i in range(3,k):
        a,b=diff(i)
        if (b+1)%3==0 and a%3==0:
            print("(",(b+1)/3,",", a/3,")")