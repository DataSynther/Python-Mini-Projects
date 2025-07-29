# GCD function following Euclid Law 
def gcd(a,b):
    while a != 0:
        a,b = b%a, a

# Modular inverse function using extended Euclid's Law
def find_mod_inverse(a,m):
    if gcd(a,m) != 1 :
        return None # No mod inverse if a and m aren't relative prime
    
    u1,u2,u3 = 1,0,a
    v1, v2, v3 = 0,1,m

    while v3 != 0:
        q = u3//v3 # Note that // is the integer dividion operator
        v1, v2, v3, u1,u2,u3 = (u1 - (q*v1)),(u2 - (q*v2)),(u3 - (q*v3)),v1,v2,v3
    
    return u1 % m