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
                return ((i-1),2**(i-1)+1)
                break
    
    def diff(n):
         a,b=ll(n)
         c,d=prob(0,n)
         
         return ((a*d-c*b)/math.gcd((a*d-c*b),(d*b))),((d*b)/math.gcd((a*d-c*b),(d*b)))
         
    n=int(input("Enter range: "))
    
    print(diff(n))
    
    
    
    def check():
        a,b=diff(n)
        
        if (a-1)%3==0 and b%3==0:
            print("Yes, numerator=3n+1 and denominator=3k")
            print((a-1)/3, b/3)
        elif (a+1)%3==0 and b%3==0:
            print("Yes, numerator=3n-1 and denominator=3k")
            print((a+1)/3, b/3)
        elif (b+1)%3==0 and a%3==0:
            print("Yes, numerator=3n, denominator=3k-1")
            print((b+1)/3, a/3)
        elif (b-1)%3==0 and a%3==0:
            print("Yes, numerator=3n, denominator=3k+1")
            print((b-1)/3, a/3)
        elif math.gcd(int(a),int(b))==1:
            print("Yes, coprimes")
            
    c1=input("Want to test conjecture type Y/N?: ")
    
    if c1 in "Yy":
        check()
    elif c1 in "Nn":
        print("Ah, confident kid, continue")
            
    
